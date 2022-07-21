CREATE PROCEDURE getAllEntriesOfUser(IN user_id INT) BEGIN DECLARE done INT;

DECLARE bank_id INT;

DECLARE cur_bank CURSOR FOR
SELECT
  ID
FROM
  banks
WHERE
  ID_USER = user_id;

DECLARE CONTINUE HANDLER FOR NOT FOUND
SET
  done = 1;

DROP TEMPORARY TABLE IF EXISTS entries_by_user;

CREATE TEMPORARY TABLE entries_by_user (
  ID INT,
  ID_BANK INT,
  ID_CATEGORY_TYPE INT,
  DATE DATE,
  VALUE FLOAT(2),
  OBSERVATION VARCHAR(255),
  CREATED_AT DATETIME,
  UPDATED_AT DATETIME
);

OPEN cur_bank;

SET
  done = 0;

REPEAT FETCH cur_bank INTO bank_id;

INSERT INTO
  entries_by_user (
    ID,
    ID_BANK,
    ID_CATEGORY_TYPE,
    DATE,
    VALUE,
    OBSERVATION,
    CREATED_AT,
    UPDATED_AT
  )
SELECT
  ID,
  ID_BANK,
  ID_CATEGORY_TYPE,
  DATE,
  VALUE,
  OBSERVATION,
  CREATED_AT,
  UPDATED_AT
FROM
  entries
WHERE
  ID_BANK = bank_id;

UNTIL done
END REPEAT;

CLOSE cur_bank;

SELECT
  *
FROM
  entries_by_user;

END;