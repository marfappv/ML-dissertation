drop schema if exists wga;
go  --GO keyword splits the statement into separate batches

create schema wga;
go

drop table if exists wga.staff;
create table wga.staff (
	Staff_ID  int identity (1,1) not null, constraint PK_Staff_ID primary key clustered (Staff_ID),
	Synergy_Team						varchar(100),
	Employment_Total_Months				int
);
go

drop table if exists wga.projects;
create table wga.projects(
    Project_ID decimal identity (1,1) not null, constraint PK_Project_ID primary key clustered (Project_ID),
	Country								varchar(100),
	Office								varchar(100),
	Sector                              varchar(100),
	Project_Size_Sort_Order             int,
	Is_Multi_Discipline_Project         bit,
	Is_First_Client_Project             bit,
	Default_Rate_Group					varchar(100),
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
alter table wga.projects
add constraint Project_Manager foreign key (Project_Manager) references wga.staff(Staff_ID);
alter table wga.projects
add constraint Project_Director foreign key (Project_Director) references wga.staff(Staff_ID);  
go

drop table if exists wga.stages;
create table wga.stages (
	Project_ID							decimal,
    Stage_ID                            int, 
	Stage_Status_Sort_Order             float,
	Is_Disbursement_Stage				bit,
    Stage_Fee_Type                      varchar(100),
	Stage_Manager						varchar(100),
    Stage_Discipline                    varchar(100),
	Stage_Duration_Weeks				int
);
alter table wga.stages
add foreign key (Project_ID) references wga.projects(Project_ID);
go

drop table if exists wga.clients;
create table wga.clients (
	Client_ID							int,
    Client_Projects_Total_No            int,
    Client_First_Project_ID				decimal,
	Is_Repeated                         bit,
	Is_Recent							bit,
	Client_Duration_Months				int
);
alter table wga.clients
add foreign key (Client_First_Project_ID) references wga.projects(Project_ID);
go