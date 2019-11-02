BEGIN TRANSACTION;
CREATE TABLE `Services` (
	`id`	INTEGER,
	`name`	TEXT,
	`location`	TEXT,
	PRIMARY KEY(id)
);
INSERT INTO `Services` (id,name,location) VALUES (1,'Siège','Ecouelès'),
 (2,'Agence1','Orbana');
CREATE TABLE "Employees" (
	`registration_number`	INTEGER,
	`name`	TEXT,
	`first_name`	TEXT,
	`birth_date`	TEXT,
	`email`	TEXT,
	`home_phone_number`	TEXT,
	`cellphone_number`	TEXT,
	`id_service`	INTEGER,
	PRIMARY KEY(registration_number)
);
INSERT INTO `Employees` (registration_number,name,first_name,birth_date,email,home_phone_number,cellphone_number,id_service) VALUES (1,'de Savoie','Tom','08/08/1908','tds@lab.bha','555-08-08','666-08-08',1),
 (2,'Heurdegase','Aude','07/07/2007','af@lab.bha','555-07-07','666-07-07',2),
 (3,'Térieur','Alain','06/06/1996','at@lab.bha','555-06-06','666-06-06',1);
COMMIT;
