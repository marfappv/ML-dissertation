drop schema if exists aec;
go  --GO keyword splits the statement into separate batches

create schema aec;
go

drop table if exists aec.staff;
create table aec.staff (
	Staff_ID 							int identity (1,1) not null, constraint PK_Staff_ID primary key clustered (Staff_ID),
	Synergy_Team						varchar(31),
	Employment_Total_Months				int
);
go

drop table if exists aec.health;
create table aec.health (
	Project_ID 							int,
	Stage_ID							int,
	DQ_Has_Issues						bit,
	DQ_Has_Inactive_Staff_Resourced		bit,
	Health_Perc_Duration_Complete		float,
	Health_Perc_Fee_Used				float,
	Alerts_Total_Per_Project			int,
	Alerts_Total_Per_Stage				int
);

drop table if exists aec.projects;
create table aec.projects(
    Project_ID 							int identity (1,1) not null, constraint PK_Project_ID primary key clustered (Project_ID),
	Country								varchar(20),
	Office								varchar(38),
	Sector                              varchar(41),
	Project_Size_Sort_Order             int,
	Is_Multi_Discipline_Project         bit,
	Is_First_Client_Project             bit,
	Default_Rate_Group					varchar(12),
	Perc_of_Stages_with_Fixed_Fee       float,
	Project_Manager                     int,
	Manager_Is_Recent					bit,
	Project_Director                    int,
	Perc_of_Subcontractors				float, 
	Project_Duration_Weeks              int,
	Is_Front_Loaded						bit,
	Delivered_on_Time                   bit,
	Fully_In_Lockdown					bit,
	Partially_In_Lockdown				bit,
	Suffered_Data_Loss                  bit,
	Total_Data_Issues					int
);
alter table aec.projects
add constraint Project_Manager foreign key (Project_Manager) references aec.staff(Staff_ID);
alter table aec.projects
add constraint Project_Director foreign key (Project_Director) references aec.staff(Staff_ID);
go

drop table if exists aec.stages;
create table aec.stages (
	Project_ID							int,
	Stage_ID 							int identity (1,1) not null, constraint PK_Stage_ID primary key clustered (Stage_ID),
	Stage_Status_Sort_Order             float,
	Is_Disbursement_Stage				bit,
    Stage_Fee_Type                      varchar(19),
	Stage_Manager						varchar(23),
    Stage_Discipline                    varchar(20),
	Stage_Duration_Weeks				int,
	Total_Data_Issues					int
);
alter table aec.stages
add foreign key (Project_ID) references aec.projects(Project_ID);
add foreign key (Stage_ID) references aec.stages(Stage_ID);
go

alter table aec.health
add foreign key (Project_ID) references aec.projects(Project_ID);
add foreign key (Stage_ID) references aec.stages(Stage_ID);
add foreign key (Alerts_Total_Per_Project) references aec.projects(Total_Data_Issues);
add foreign key (Alerts_Total_Per_Stage) references aec.stages(Total_Data_Issues);
go

drop table if exists aec.clients;
create table aec.clients (
	Client_ID							int identity (1,1) not null, constraint PK_Client_ID primary key clustered (Client_ID),
    Client_Projects_Total_No            int,
    Client_First_Project_ID				int,
	Is_Repeated                         bit,
	Is_Recent							bit,
	Client_Duration_Months				int
);
alter table aec.clients
add foreign key (Client_First_Project_ID) references aec.projects(Project_ID);
go

drop table if exists aec.transactions;
create table aec.transactions (
	Transaction_ID 						int identity (1,1) not null, constraint PK_Transaction_ID primary key clustered (Transaction_ID),
	Project_ID 							int,
	Stage_ID							int,
	Transaction_Type					varchar(7),
	Rate_Type							varchar(14),
	Status								varchar(11),
	Units								float,
	Value_Total							float,
	Invoice_Value_Total					float,
	Actual_Cost_Total					float,
	Target_Charge_Total					float,
	Date								timestamp
);
alter table aec.transactions
add foreign key (Project_ID) references aec.projects(Project_ID);
add foreign key (Stage_ID) references aec.stages(Stage_ID);
go