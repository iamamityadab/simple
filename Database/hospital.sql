-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 06, 2022 at 11:42 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `adminid` varchar(40) DEFAULT NULL,
  `adminpwd` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`adminid`, `adminpwd`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `appointments`
--

CREATE TABLE `appointments` (
  `id` varchar(10) DEFAULT NULL,
  `appnum` varchar(40) DEFAULT NULL,
  `type` varchar(40) DEFAULT NULL,
  `date1` varchar(40) DEFAULT NULL,
  `descr` varchar(40) DEFAULT NULL,
  `doctor_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointments`
--

INSERT INTO `appointments` (`id`, `appnum`, `type`, `date1`, `descr`, `doctor_id`) VALUES
(5, '5', '743r436', '59', '5', 2),
(9, '9', '32849', '2022-05-18', 'jhj', 2),
(1, '4746587', 'ur hguh', '2022-06-09', 'kdflsn bsj', 3),
(11, '3472594', 'dfbnjnb', '2022-06-19', 'nnfgdsjfbgjbz', 2);

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `id` varchar(10) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `mobile` varchar(40) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `address` varchar(40) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL,
  `username` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`id`, `name`, `mobile`, `email`, `address`, `password`, `username`) VALUES
(3, '7', '58', '88', '5', '5', '5'),
(2, 'Achal', '06207020459', 'kumarachal104@gmail.com', 'Village-Kharhar,', '39', '2');

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

CREATE TABLE `hospital` (
  `id` varchar(10) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `type` varchar(40) DEFAULT NULL,
  `descr` varchar(40) DEFAULT NULL,
  `place` varchar(40) DEFAULT NULL,
  `address` varchar(40) DEFAULT NULL,
  `doctor_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital`
--

INSERT INTO `hospital` (`id`, `name`, `type`, `descr`, `place`, `address`, `doctor_id`) VALUES
(1, '4', '4', '4', '4', '4', 2),
(2, '2', '2', '2', '2', '2', 2),
(5, 'g', '5', '5', '5', '5', 2),
(3, 'lmV', 'lkdafncjdsb', 'e;lwmfkren', ',ad f dcdas a', 'kfdnjrs', 3);

-- --------------------------------------------------------

--
-- Table structure for table `inquiry`
--

CREATE TABLE `inquiry` (
  `name` varchar(20) DEFAULT NULL,
  `number` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `descr` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inquiry`
--

INSERT INTO `inquiry` (`name`, `number`, `email`, `descr`) VALUES
('kjbcjhSD2734', '737437', 'kjbddsjfhv', 'hewgjhe'),
('znxbcnzuryu432478', '38242', 'fidjg', 'jfhdjksfb'),
('jkkj', 'hjgjhg', 'kjhkh', 'kjhhjkj'),
('kalsdas213', 'hjgjhg', 'kjhkh', 'kjhhjkj'),
('kalsdas213', '32432', 'kjhkh', 'kjhhjkj'),
('Achal Kumar', '06207020455', 'kjhkh', 'kjhhjkj'),
('Achal Kumar', '06207020455', 'kumarachal104@gmail.', 'kjhhjkj'),
('Achal Kumar', '06207020455', 'kumarachal104@gmail.', 'kjhhjkj'),
('Achal Kumar', '06207020455', 'kumarachal104@gmail.', 'ljghfjcgc');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `logid` varchar(40) DEFAULT NULL,
  `logpwd` varchar(40) DEFAULT NULL,
  `counter` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`logid`, `logpwd`, `counter`) VALUES
('hospital', 'hospital', 41),
(NULL, NULL, 4),
('achal', 'achal', 8),
('achal', 'achal', 8),
('hospital', 'hospital', 41),
('hospital', 'hospital', 41),
('rahul', 'rahul', 0);

-- --------------------------------------------------------

--
-- Table structure for table `medicines`
--

CREATE TABLE `medicines` (
  `id` varchar(10) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `company` varchar(40) DEFAULT NULL,
  `cost` varchar(40) DEFAULT NULL,
  `type` varchar(40) DEFAULT NULL,
  `descr` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medicines`
--

INSERT INTO `medicines` (`id`, `name`, `company`, `cost`, `type`, `descr`) VALUES
(1, '5', '5', '5', '5', '5'),
(1, '5', '5', '5', '5', '5'),
(2, '2', '2', '2', '2', '2'),
(3467, 'Ahs', 'hudsgf', '876765.89', 'ufh', 'idhf'),
(246, 'kjdg', 'kjaf', '2000.877', 'lkfgn', 'kg'),
(249, 'kjdg', 'kjaf', '2000.8776', 'lkfgn', 'kg'),
(248, 'kjdg', 'kjaf', '2000.87768', 'lkfgn', 'kg');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `id` varchar(10) DEFAULT NULL,
  `mobile` varchar(40) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `address` varchar(40) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL,
  `username` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`id`, `mobile`, `name`, `email`, `address`, `password`, `username`) VALUES
(1, '3', '3', '3', '33', '3', '3'),
(2, '2', '2', '2', '2', '2', '2');

-- --------------------------------------------------------

--
-- Table structure for table `permission`
--

CREATE TABLE `permission` (
  `id` varchar(10) DEFAULT NULL,
  `roll_id` varchar(10) DEFAULT NULL,
  `title` varchar(40) DEFAULT NULL,
  `module` varchar(40) DEFAULT NULL,
  `descr` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `permission`
--

INSERT INTO `permission` (`id`, `roll_id`, `title`, `module`, `descr`) VALUES
(1, 3, '3', '3', '3'),
(2, 2, '2', '2', '2'),
(5, 2, '5', '5', '5');

-- --------------------------------------------------------

--
-- Table structure for table `roll`
--

CREATE TABLE `roll` (
  `id` varchar(10) DEFAULT NULL,
  `roll_title` varchar(40) DEFAULT NULL,
  `roll_descr` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roll`
--

INSERT INTO `roll` (`id`, `roll_title`, `roll_descr`) VALUES
(1, '3', '3'),
(2, '2', '2');

-- --------------------------------------------------------

--
-- Table structure for table `user1`
--

CREATE TABLE `user1` (
  `id` varchar(10) DEFAULT NULL,
  `roll_id` varchar(10) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `address` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user1`
--

INSERT INTO `user1` (`id`, `roll_id`, `name`, `email`, `dob`, `address`) VALUES
(1, 3, '3', '3', '3', '3'),
(2, 2, '2', '2', '2', '2'),
(5, 2, 'g', '5', '5', '5');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
