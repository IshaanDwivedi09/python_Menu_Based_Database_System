-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 02, 2019 at 07:42 PM
-- Server version: 5.7.19
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alpha`
--
CREATE DATABASE IF NOT EXISTS `alpha` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `alpha`;

-- --------------------------------------------------------

--
-- Table structure for table `admission_data`
--

DROP TABLE IF EXISTS `admission_data`;
CREATE TABLE IF NOT EXISTS `admission_data` (
  `adno` varchar(100) DEFAULT NULL,
  `rno` varchar(100) DEFAULT NULL,
  `sname` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phon` varchar(100) DEFAULT NULL,
  `clas` varchar(100) DEFAULT NULL,
  `sec` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `fee_database`
--

DROP TABLE IF EXISTS `fee_database`;
CREATE TABLE IF NOT EXISTS `fee_database` (
  `session` varchar(100) DEFAULT NULL,
  `stclass` varchar(100) DEFAULT NULL,
  `stsec` varchar(100) DEFAULT NULL,
  `stroll` varchar(100) DEFAULT NULL,
  `paymenttype` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `dat` date DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fee_database`
--

INSERT INTO `fee_database` (`session`, `stclass`, `stsec`, `stroll`, `paymenttype`, `amount`, `dat`) VALUES
('2019-20', '12', 'Science', '18', 'Tuition', 'Rs. 5,040', '2019-10-09'),
('2019-20', '12', 'Science', '10', 'Travel', 'Rs. 4,040', '2019-12-30');

-- --------------------------------------------------------

--
-- Table structure for table `student_database`
--

DROP TABLE IF EXISTS `student_database`;
CREATE TABLE IF NOT EXISTS `student_database` (
  `session` varchar(100) DEFAULT NULL,
  `stname` varchar(100) DEFAULT NULL,
  `stclass` varchar(100) DEFAULT NULL,
  `stsec` varchar(100) DEFAULT NULL,
  `stroll` varchar(100) DEFAULT NULL,
  `sub1` varchar(100) DEFAULT NULL,
  `sub2` varchar(100) DEFAULT NULL,
  `sub3` varchar(100) DEFAULT NULL,
  `sub4` varchar(100) DEFAULT NULL,
  `sub5` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_database`
--

INSERT INTO `student_database` (`session`, `stname`, `stclass`, `stsec`, `stroll`, `sub1`, `sub2`, `sub3`, `sub4`, `sub5`) VALUES
('2019-20', 'Ishaan Dwivedi', '12', 'Science', '18', 'Physics', 'Chemistry', 'Mathematics', 'Computer', 'English');

-- --------------------------------------------------------

--
-- Table structure for table `teacher_database`
--

DROP TABLE IF EXISTS `teacher_database`;
CREATE TABLE IF NOT EXISTS `teacher_database` (
  `year` varchar(100) DEFAULT NULL,
  `tename` varchar(100) DEFAULT NULL,
  `teclass` varchar(100) DEFAULT NULL,
  `tesalary` varchar(100) DEFAULT NULL,
  `teid` varchar(100) DEFAULT NULL,
  `sub` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
