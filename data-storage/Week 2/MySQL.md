# Week 2: MySQL Basic Commands

#### Write an SQL statement to create a simple table `countries` including columns `country_id`,`country_name` and `region_id`.

```sql
CREATE TABLE `countries` (
  `country_id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `country_name` varchar(50) NOT NULL,
  `region_id` int NOT NULL
);
```

#### Write an SQL statement to insert a record with your own value into the table `countries` against each column.

```sql
INSERT INTO `countries` (`country_name`, `region_id`) VALUES ('Romania', '3');
INSERT INTO `countries` (`country_name`, `region_id`) VALUES ('Finland', '10');
INSERT INTO `countries` (`country_name`, `region_id`) VALUES ('England', '11');
```

#### Write an SQL statement to `insert` records into the table `countries` to ensure that the `country_id` column will `not` contain any duplicate data and this will be automatically incremented and the column `country_name` will be filled up by `N/A` if no value assigned for that column.

```sql
ALTER TABLE `countries` CHANGE `country_name` `country_name` varchar(50) NULL DEFAULT 'N/A' AFTER `country_id`;
```

#### Write an SQL statement to `change` the `email` column of `employees` table with `not available` for all employees.

```sql
UPDATE `employees` SET email = 'not available';
```

#### Write an SQL statement to `change` the `email` column of `employees` table with 'not available' for those employees whose `department_id` is `80` and gets a `commission` is `less than` `.20%`.

```sql
UPDATE employees
SET email = 'not available'
WHERE department_id = 80 AND commision_pct < 0.20;
```

#### Write an SQL statement to `add` a column `region_id` to the table `locations`.

```sql
ALTER TABLE `locations`
ADD `region_id` int(11);
```

#### Write an SQL statement to `drop` the column `city` from the table `locations`.

```sql
ALTER TABLE `locations`
DROP `city`;
```

#### Write an SQL statement to `add` a `primary key` for the columns `location_id` in the `locations` table.

```sql
ALTER TABLE `locations` ADD PRIMARY KEY (location_id);
```