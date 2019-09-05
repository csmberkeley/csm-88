CREATE TABLE records AS
    SELECT "Ben Bitdiddle" AS name, "Computer" AS division, "Wizard" AS title,
        60000 AS salary, "Oliver Warbucks" AS supervisor UNION
    SELECT "Alyssa P Hacker", "Computer", "Programmer", 40000, "Ben Bitdiddle" UNION
    SELECT "Cy D Fect", "Computer", "Programmer", 35000, "Ben Bitdiddle" UNION
    SELECT "Lem E Tweakit", "Computer", "Technician", 25000, "Ben Bitdiddle" UNION
    SELECT "Louis Reasoner", "Computer", "Programmer Trainee", 30000, "Alyssa P Hacker" UNION
    SELECT "Oliver Warbucks", "Administration", "Big Wheel", 150000, "Oliver Warbucks" UNION
    SELECT "Eben Scrooge", "Accounting", "Chief Accountant", 75000, "Oliver Warbucks" UNION
    SELECT "Robert Cratchet", "Accounting", "Scrivener", 18000, "Eben Scrooge";

CREATE TABLE meetings AS
    SELECT "Accounting" AS division, "Monday" AS day, "9am" AS time UNION
    SELECT "Computer", "Wednesday", "4pm" UNION
    SELECT "Administration", "Monday", "11am" UNION
    SELECT "Administration", "Wednesday", "4pm";
