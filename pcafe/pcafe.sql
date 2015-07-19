-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jul 18, 2015 at 04:13 PM
-- Server version: 5.5.43-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `pcafe`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=175 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add user details', 7, 'add_userdetails'),
(20, 'Can change user details', 7, 'change_userdetails'),
(21, 'Can delete user details', 7, 'delete_userdetails'),
(22, 'Can add user address', 8, 'add_useraddress'),
(23, 'Can change user address', 8, 'change_useraddress'),
(24, 'Can delete user address', 8, 'delete_useraddress'),
(25, 'Can add categories', 9, 'add_categories'),
(26, 'Can change categories', 9, 'change_categories'),
(27, 'Can delete categories', 9, 'delete_categories'),
(55, 'Can add feed back', 19, 'add_feedback'),
(56, 'Can change feed back', 19, 'change_feedback'),
(57, 'Can delete feed back', 19, 'delete_feedback'),
(58, 'Can add order tracking table', 20, 'add_ordertrackingtable'),
(59, 'Can change order tracking table', 20, 'change_ordertrackingtable'),
(60, 'Can delete order tracking table', 20, 'delete_ordertrackingtable'),
(61, 'Can add area details', 21, 'add_areadetails'),
(62, 'Can change area details', 21, 'change_areadetails'),
(63, 'Can delete area details', 21, 'delete_areadetails'),
(64, 'Can add contact us', 22, 'add_contactus'),
(65, 'Can change contact us', 22, 'change_contactus'),
(66, 'Can delete contact us', 22, 'delete_contactus'),
(169, 'Can add sub categories', 57, 'add_subcategories'),
(170, 'Can change sub categories', 57, 'change_subcategories'),
(171, 'Can delete sub categories', 57, 'delete_subcategories'),
(172, 'Can add items_ menu', 58, 'add_items_menu'),
(173, 'Can change items_ menu', 58, 'change_items_menu'),
(174, 'Can delete items_ menu', 58, 'delete_items_menu');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=59 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(21, 'pcafeapp', 'areadetails'),
(9, 'pcafeapp', 'categories'),
(22, 'pcafeapp', 'contactus'),
(19, 'pcafeapp', 'feedback'),
(58, 'pcafeapp', 'items_menu'),
(20, 'pcafeapp', 'ordertrackingtable'),
(57, 'pcafeapp', 'subcategories'),
(8, 'pcafeapp', 'useraddress'),
(7, 'pcafeapp', 'userdetails'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=59 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2015-07-16 06:35:50'),
(2, 'auth', '0001_initial', '2015-07-16 06:35:50'),
(3, 'admin', '0001_initial', '2015-07-16 06:35:50'),
(4, 'contenttypes', '0002_remove_content_type_name', '2015-07-16 06:35:50'),
(5, 'auth', '0002_alter_permission_name_max_length', '2015-07-16 06:35:50'),
(6, 'auth', '0003_alter_user_email_max_length', '2015-07-16 06:35:50'),
(7, 'auth', '0004_alter_user_username_opts', '2015-07-16 06:35:50'),
(8, 'auth', '0005_alter_user_last_login_null', '2015-07-16 06:35:50'),
(9, 'auth', '0006_require_contenttypes_0002', '2015-07-16 06:35:50'),
(10, 'pcafeapp', '0001_initial', '2015-07-16 06:35:51'),
(11, 'sessions', '0001_initial', '2015-07-16 06:35:51'),
(12, 'pcafeapp', '0002_remove_contactus_pobox', '2015-07-16 06:40:21'),
(13, 'pcafeapp', '0003_auto_20150716_1028', '2015-07-16 10:28:58'),
(14, 'pcafeapp', '0004_bf_fruits_grains_menu_breakfast_subcat', '2015-07-16 10:48:25'),
(15, 'pcafeapp', '0005_auto_20150716_1050', '2015-07-16 10:50:43'),
(16, 'pcafeapp', '0006_bf_sandwitches', '2015-07-16 10:59:45'),
(17, 'pcafeapp', '0007_bf_morning_meals', '2015-07-16 11:10:09'),
(18, 'pcafeapp', '0008_bf_organic_eggs', '2015-07-16 11:15:24'),
(19, 'pcafeapp', '0009_bf_sweets', '2015-07-16 11:22:59'),
(20, 'pcafeapp', '0010_bf_sides', '2015-07-16 11:25:43'),
(21, 'pcafeapp', '0011_lm_salads', '2015-07-16 11:37:24'),
(22, 'pcafeapp', '0012_lm_shareables', '2015-07-16 11:43:12'),
(23, 'pcafeapp', '0013_lm_sandwitches_burgers', '2015-07-16 11:48:16'),
(24, 'pcafeapp', '0014_mains_grills_mains', '2015-07-16 12:41:32'),
(25, 'pcafeapp', '0015_auto_20150716_1310', '2015-07-16 13:10:47'),
(26, 'pcafeapp', '0016_mains_grills_sides', '2015-07-16 13:15:40'),
(27, 'pcafeapp', '0017_kids_breakfast', '2015-07-16 13:25:07'),
(28, 'pcafeapp', '0018_kids_mains', '2015-07-16 14:01:01'),
(29, 'pcafeapp', '0019_pizzamenu', '2015-07-16 14:06:13'),
(30, 'pcafeapp', '0020_dessertsmenu', '2015-07-16 14:16:36'),
(31, 'pcafeapp', '0021_tea_coffes_hot_coffee', '2015-07-16 14:22:21'),
(32, 'pcafeapp', '0022_tea_coffes_cold_coffee', '2015-07-16 14:29:18'),
(33, 'pcafeapp', '0023_tea_coffes_tea', '2015-07-16 14:33:56'),
(34, 'pcafeapp', '0024_auto_20150716_1434', '2015-07-16 14:34:28'),
(35, 'pcafeapp', '0025_ssj_smoothies', '2015-07-16 14:42:49'),
(36, 'pcafeapp', '0026_ssj_milkshakes', '2015-07-16 14:46:47'),
(37, 'pcafeapp', '0027_ssj_sparklers', '2015-07-16 14:50:14'),
(38, 'pcafeapp', '0028_ssj_fresh_juices', '2015-07-16 14:58:20'),
(39, 'pcafeapp', '0029_breakfast_subcategories', '2015-07-17 02:17:57'),
(40, 'pcafeapp', '0030_lightmeals_subcategories', '2015-07-17 02:22:29'),
(41, 'pcafeapp', '0031_mainsgrills_subcategories', '2015-07-17 02:25:14'),
(42, 'pcafeapp', '0032_kidsmenu_subcategories', '2015-07-17 02:27:31'),
(43, 'pcafeapp', '0033_teacoffee_subcategories', '2015-07-17 02:29:23'),
(44, 'pcafeapp', '0034_ssj_subcategories', '2015-07-17 02:31:40'),
(45, 'pcafeapp', '0035_auto_20150717_0625', '2015-07-17 06:25:40'),
(46, 'pcafeapp', '0036_ssj_bottled_juices', '2015-07-17 07:14:44'),
(47, 'pcafeapp', '0037_auto_20150717_0717', '2015-07-17 07:17:11'),
(48, 'pcafeapp', '0038_ordertrackingtable_sub_cat_id', '2015-07-17 09:35:23'),
(49, 'pcafeapp', '0039_auto_20150717_0950', '2015-07-17 09:51:02'),
(50, 'pcafeapp', '0040_auto_20150717_1050', '2015-07-17 10:50:38'),
(51, 'pcafeapp', '0041_auto_20150717_1051', '2015-07-17 10:51:05'),
(52, 'pcafeapp', '0042_auto_20150717_1316', '2015-07-17 13:17:05'),
(53, 'pcafeapp', '0043_auto_20150717_1643', '2015-07-17 16:43:59'),
(54, 'pcafeapp', '0044_auto_20150717_1644', '2015-07-17 16:44:06'),
(55, 'pcafeapp', '0045_auto_20150717_1659', '2015-07-17 16:59:28'),
(56, 'pcafeapp', '0046_ordertrackingtable_recieve_time', '2015-07-17 17:03:27'),
(57, 'pcafeapp', '0047_userdetails_verification_code', '2015-07-18 06:29:50'),
(58, 'pcafeapp', '0048_auto_20150718_0643', '2015-07-18 06:43:32');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4bflbqmrrewcqdash2zf9ktuwytcbevd', 'NTk1ZWE2MmJiMWNjYjZlODI1NDNmNWQ2N2M1YzM3MmY3ZWYwZmFkMzqAAn1xAShVB29yZGVyaWRxAk0ZEVUHZ3Vlc3RpZHEDTdQPdS4=', '2015-07-31 17:01:05'),
('6vif7m5f9nt9nbo36uj2366nx24ggdv0', 'NzE0ZDAwN2ViNjJkMDQ1YzI5MzU2YWIwZTMzNDJmYzk2Yjc2NTY5NDqAAn1xAShVB2d1ZXN0aWRNBBlVBnVzZXJpZHECY2RqYW5nby5kYi5tb2RlbHMuYmFzZQptb2RlbF91bnBpY2tsZQpxA1UIcGNhZmVhcHBxBFULVXNlckRldGFpbHNxBYZdY2RqYW5nby5kYi5tb2RlbHMuYmFzZQpzaW1wbGVfY2xhc3NfZmFjdG9yeQpxBodScQd9cQgoVQlkYXRlX3RpbWVjZGF0ZXRpbWUKZGF0ZXRpbWUKcQlVCgffBwsHMwEAAABjcHl0egpfVVRDCnEKKVJxC4ZScQxVCmZpcnN0X25hbWVYBwAAAEFyYXZpbmRVCWxhc3RfbmFtZVgHAAAAR2FqZWxsaVUPX2RqYW5nb192ZXJzaW9uVQUxLjguMVUGX3N0YXRlY2RqYW5nby5kYi5tb2RlbHMuYmFzZQpNb2RlbFN0YXRlCnENKYFxDn1xDyhVBmFkZGluZ3EQiVUCZGJxEVUHZGVmYXVsdHViVQdjb21wYW55WAAAAABoAooBFFUJaXNfYWN0aXZliVUKaG93X2FidF91c1gaAAAAUlNEIGRpcmVjdG9yeSBkaXN0cmlidXRpb25VCHBob25lX25vWAwAAAAxMjM1NDY4MTMxMzJVA2RvYlgKAAAAMzEvMDEvMTk5MVUGbW9iaWxlWAoAAAA5NjQwODY5NDg3VQhwYXNzd29yZFgGAAAAMTIzNDU2VQVlbWFpbFgaAAAAYXJhdmluZC5nYWplbGxpZ0BnbWFpbC5jb211YnUu', '2015-07-30 07:48:57'),
('a0m2mvlykipd6oz4f9415f8lo7vvshz9', 'ODRkNGRiMDFmZjA3MDk0OTJjMDMzZGRlNTllNTQwMmI2MGE1MTJkNDqAAn1xAShVB2d1ZXN0aWRN2xdVBnVzZXJpZHECY2RqYW5nby5kYi5tb2RlbHMuYmFzZQptb2RlbF91bnBpY2tsZQpxA1UIcGNhZmVhcHBxBFULVXNlckRldGFpbHNxBYZdY2RqYW5nby5kYi5tb2RlbHMuYmFzZQpzaW1wbGVfY2xhc3NfZmFjdG9yeQpxBodScQd9cQgoVQlkYXRlX3RpbWVjZGF0ZXRpbWUKZGF0ZXRpbWUKcQlVCgffBxIIAjQAAABjcHl0egpfVVRDCnEKKVJxC4ZScQxVCmZpcnN0X25hbWVYBwAAAEFyYXZpbmRVCWxhc3RfbmFtZVgHAAAAR2FqZWxsaVUPX2RqYW5nb192ZXJzaW9uVQUxLjguMVUGX3N0YXRlY2RqYW5nby5kYi5tb2RlbHMuYmFzZQpNb2RlbFN0YXRlCnENKYFxDn1xDyhVBmFkZGluZ3EQiVUCZGJxEVUHZGVmYXVsdHViVQdjb21wYW55WAAAAABoAooBBVURdmVyaWZpY2F0aW9uX2NvZGVYCQAAAHRsYTI5MXd6c1UJaXNfYWN0aXZliFUKaG93X2FidF91c1gFAAAARW1haWxVCHBob25lX25vWAkAAAA3ODk0NTYxMjNVA2RvYlgDAAAAMi0xVQZtb2JpbGVYCgAAADk2NDA4Njk0ODdVCHBhc3N3b3JkWAYAAAAxMjM0NTZVBWVtYWlsWBoAAABhcmF2aW5kLmdhamVsbGlnQGdtYWlsLmNvbXVidS4=', '2015-08-01 10:04:35'),
('oofvdx1l7u5k13xu26d63jjicv6ghdd2', 'MjZlNzdkYjY2MGIyN2QxYmIxNTFhYjhmYjEwZmYyOTM1ZjI5OWRlNzqAAn1xAShVB29yZGVyaWRxAk1MBFUHZ3Vlc3RpZHEDTToQdS4=', '2015-07-31 10:20:36'),
('vsrg4us46psjbcb3j0qwxchetngzwwsg', 'NDgzM2NjM2NhZWZiYjBkYWM2NDAxNjRmMTZmYzYwOWRhYmJlMmM5YjqAAn1xAShVB29yZGVyaWRNpB9VB2d1ZXN0aWRNFRJ1Lg==', '2015-07-31 13:29:21'),
('ze9x0vkssjcoe84nj735b4340qcxkkg6', 'OGUzY2NlNTA4YmY4YTI2Y2Q3YWQ3YTlmZjFmMWYyYWQyODIzYmM2NzqAAn1xAShVB29yZGVyaWRxAk2zHVUHZ3Vlc3RpZHEDTckHdS4=', '2015-07-31 16:51:14');

-- --------------------------------------------------------

--
-- Table structure for table `pcafeapp_areadetails`
--

CREATE TABLE IF NOT EXISTS `pcafeapp_areadetails` (
  `areacode` int(11) NOT NULL,
  `areaname` varchar(100) NOT NULL,
  PRIMARY KEY (`areacode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pcafeapp_areadetails`
--

INSERT INTO `pcafeapp_areadetails` (`areacode`, `areaname`) VALUES
(1, 'Deira - Abu Hail'),
(2, 'Garhood'),
(3, 'Mirdif'),
(4, 'Bur Dubai'),
(5, 'SZR - 1st - 4th Interchange'),
(6, 'Al Safa (1,2)'),
(7, 'Arabian Ranches'),
(8, 'JAFZA'),
(9, 'Al Waha Community'),
(10, 'Green Community'),
(11, 'Motor City'),
(12, 'Jumeirah Village (Circle/Triangle)'),
(13, 'Al Barari - Dubailand'),
(14, 'Al Satwa / Al Badaa'),
(15, 'Dubai Marina'),
(16, 'JLT - Jumeirah Lake Towers'),
(17, 'Greens, The'),
(18, 'TECOM'),
(19, 'DMC - Dubai Media City'),
(20, 'Al Barsha (1,2,3)'),
(21, 'Al Quoz Residential (1,2)'),
(22, 'Business Bay'),
(23, 'DIFC'),
(24, 'JBR - Jumeirah Beach Residence'),
(25, 'Jumeirah (1,2,3)'),
(26, 'Downtown Burj Khalifa'),
(27, 'Lamcy Plaza Area'),
(28, 'Oud Metha'),
(29, 'Palm Jumeirah'),
(30, 'SZR - Trade Center to 1st Interchange'),
(31, 'Umm Suqeim (1,2,3)'),
(32, 'Wafi City'),
(33, 'Ibn Battuta Mall'),
(35, 'Jaffliyah'),
(36, 'Al Nahda (1,2)'),
(37, 'Al Sufouh'),
(38, 'Al Manara'),
(39, 'Al Wasl'),
(40, 'DIC - Dubai Internet City'),
(41, 'Karama Area'),
(42, 'Knowledge Village'),
(43, 'Laiyan Community'),
(44, 'Umm Al Sheif'),
(45, 'Zaabeel'),
(82, 'Academic City'),
(83, 'Al Barsha South'),
(84, 'Al Mamzar'),
(85, 'Al Muntazah Complex'),
(86, 'Al Quoz 4 / Al Khail Gate Village'),
(87, 'Al Quoz Industrial (1,2,3,4)'),
(88, 'Al Qusais (1,2)'),
(89, 'Al Twar (1,2,3)'),
(90, 'Al Warqa (1,2)'),
(91, 'DAFZA'),
(92, 'Deira - Al Baraha'),
(93, 'Deira - Al Muteena'),
(94, 'Deira - Al Rigga'),
(95, 'Deira - Al Wuheida'),
(96, 'Deira - Creekside'),
(97, 'Deira - Hor Al Anz'),
(98, 'Deira - Muraqqabat'),
(99, 'Deira - Port Saeed'),
(100, 'DFC - Dubai Festival City'),
(101, 'Discovery Gardens'),
(102, 'Falcon City - Dubailand'),
(103, 'Villas Compound - Dubailand'),
(104, 'Emirates Hills'),
(105, 'IMPZ'),
(106, 'International City'),
(107, 'Jebel Ali Gardens'),
(108, 'Jumeirah Islands / Jumeirah Park'),
(109, 'Khawaneej Area'),
(110, 'Meadows, The'),
(111, 'Mizher 1'),
(112, 'Mizher 2'),
(113, 'Muhaisnah 1'),
(114, 'Muhaisnah 2'),
(115, 'Nad Al Hamar'),
(116, 'Nad Al Shiba (1,2,3,4)'),
(117, 'Ras Al Khor'),
(118, 'Rashidiya'),
(119, 'Silicon Oasis'),
(120, 'Sports City'),
(121, 'Springs, The'),
(122, 'Lakes, The'),
(123, 'Deira - Naif'),
(124, 'Al Mina'),
(125, 'Al Hudaiba'),
(126, 'ZZ-1 (Wafi City)'),
(127, 'ZZ-2 (Deira Creek)'),
(128, 'ZZ-3 (Jumeirah / Beach Road)'),
(129, 'ZZ-4 (Dubai Mall / Downtown Burj)'),
(130, 'ZZ-5 (Dubai Marina / JBR)'),
(131, 'ZZ-6 (Garhoud)'),
(132, 'Jumeirah Golf Estates');

-- --------------------------------------------------------

--
-- Table structure for table `pcafeapp_categories`
--

CREATE TABLE IF NOT EXISTS `pcafeapp_categories` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(50) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `pcafeapp_categories`
--

INSERT INTO `pcafeapp_categories` (`category_id`, `category_name`) VALUES
(1, 'BREAKFAST'),
(2, 'LIGHT MEALS'),
(3, 'MAINS & GRILLS'),
(4, 'PIZZA'),
(5, 'KIDS MENU'),
(6, 'DESSERTS'),
(7, 'TEA & COFFEES'),
(8, 'SHAKES, SMOOTHIES & JUICES');

-- --------------------------------------------------------

--
-- Table structure for table `pcafeapp_contactus`
--

CREATE TABLE IF NOT EXISTS `pcafeapp_contactus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `company` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `comments` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `pcafeapp_feedback`
--

CREATE TABLE IF NOT EXISTS `pcafeapp_feedback` (
  `feedbackid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `message` varchar(200) NOT NULL,
  PRIMARY KEY (`feedbackid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `pcafeapp_items_menu`
--

CREATE TABLE IF NOT EXISTS `pcafeapp_items_menu` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_cat_id` int(11) DEFAULT NULL,
  `item_name` varchar(50) DEFAULT NULL,
  `ingrediants` varchar(200) NOT NULL,
  `price` varchar(25) DEFAULT NULL,
  `cat_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=162 ;

--
-- Dumping data for table `pcafeapp_items_menu`
--

INSERT INTO `pcafeapp_items_menu` (`item_id`, `sub_cat_id`, `item_name`, `ingrediants`, `price`, `cat_id`) VALUES
(1, 1, 'Fresh Fruits (v) (gf)', 'selection of fresh fruits, cream or low-fat yogurt', '40', 1),
(2, 1, 'Home-Made Granola (v)', 'organic oats, good-for-you seeds, coconut, honey, low-fat\\r\\nyoghurt, Sarabeth''''s preserve or home-made berry compote', '30', 1),
(3, 1, 'Quinoa Porridge (v)(gf)', 'chia seeds, coconut milk, goji berries, peaches, toasted coconut', '30', 1),
(4, 1, 'Spiced Strawberry Bircher Muesli (v)', 'low fat yoghurt, fresh pear, spiced strawberries', '30', 1),
(8, 2, 'Pantry Breakfast Burger', 'fried organic egg, beef tomato, turkey ham, aged cheddar,\r\navocado salsa, spicy mayo, brioche bun, side salad', '48', 1),
(9, 2, 'Roasted Eggplant Sandwich (v)', 'sriracha, ricotta, roasted red pepper & tomato chutney, rocket,\r\nmulti seed bread, side salad', '48', 1),
(10, 2, 'New-York Style Bagel Sandwich', 'bacon, fried organic egg, aged cheddar', '44', 1),
(11, 2, 'Turkey Ham & Cheese Croissant', 'turkey ham, brie, caramelised onions', '36', 1),
(12, 2, 'Tuna Sandwich', 'sweet corn, coriander, chillies, mayo, multi seed baguette, side\r\nsalad', '48', 1),
(13, 3, 'Fried Green Tomatoes & Buffalo Mozzarella (v)', 'avocado, sweet lemon dressing, sourdough baguette', '48', 1),
(14, 3, 'Go Healthy', 'two egg whites (poached), asparagus, grilled portobello,\r\ntomatoes, turkey ham, quinoa & chia porridge, fresh orange juice,\r\ntea or coffee', '80', 1),
(15, 3, 'Grilled Portobello Mushrooms (v)', 'spinach, corn, emmental & panko crumbs, Neapolitan sauce', '52', 1),
(16, 3, 'The Full English', 'two organic eggs (cooked any style), choice of sausages, bacon,\r\nbaked beans, grilled portobello, AOP butter, toasted rustic or\r\nwholewheat bread, fresh orange juice, tea or coffee', '80', 1),
(17, 3, 'Waffles (v)', 'mushrooms, feta, semi dried tomatoes, rocket, balsamic reduction', '45', 1),
(18, 4, 'Poached Eggs on Muffin', 'toasted wheat germ English muffin, lemon hollandaise', '46', 1),
(19, 4, 'Classic Eggs', 'two eggs (cooked any style), AOP butter, toasted rustic or\r\nwholewheat bread', '34', 1),
(20, 4, 'Smokey Tomato & Chipotle Scramble', 'spicy chipotle, Mexican beans, crème fraiche, multi seed bread', '48', 1),
(21, 4, 'Spinach & Parmesan Scramble', 'bechamel, Parmigiano Reggiano, crispy kale, toasted rustic bread', '48', 1),
(22, 4, 'Truffled Wild Mushrooms on Toast', 'poached organic egg, truffle oil, sourdough baguette', '48', 1),
(23, 4, 'Shakshouka', 'organic eggs, spicy tomato sauce, crumbled feta, jalapeños, pita Add wagyu meatballs (feta is replaced with Parmigiano Reggiano) for an additional AED 13', '52', 1),
(24, 4, 'Chicken Chorizo Omelet', 'manchego cheese, caramelised red onions, AOP butter, toasted rustic bread, house salad', '56', 1),
(25, 4, 'Roasted Red Pepper Omelet', 'mushrooms, gruyere, AOP butter, toasted rustic bread, side salad', '56', 1),
(26, 4, 'Sweet Potato Omelet ', 'tarragon, goat cheese, AOP butter, toasted rustic bread, side salad', '56', 1),
(27, 4, 'Masala Omelet', 'egg whites, tomatoes, green chillies, onion, aged cheddar, herbs, AOP butter, toasted rustic bread, house salad', '48', 1),
(28, 5, 'Crepes', 'Valrhona dark chocolate, dulcey chocolate, whipped cream', '38', 1),
(29, 5, 'Waffles', 'mixed berries, crème pâtissière, vanilla crème anglaise', '45', 1),
(30, 5, 'French Toast', 'berry compote, mascarpone, maple syrup, vanilla crème anglaise', '38', 1),
(31, 5, 'Pancakes', 'ricotta, maple syrup, caramelized banana, whipped cream', '34', 1),
(32, 6, 'Bagel', '', '10', 1),
(33, 6, 'Baked Beans', '', '8', 1),
(34, 6, 'Beef: Bacon', '', '18', 1),
(35, 6, 'Sausages', '', '16', 1),
(36, 6, 'Cheese', '(emmental, cheddar, gruyere, manchego, feta, cream cheese)', '12', 1),
(37, 6, 'Chicken: Chorizo', '', '16', 1),
(38, 6, 'Sausages', '', '10', 1),
(39, 6, 'Creamed Spinach', '', '16', 1),
(40, 6, ' Sauteed Baby Potatoes', '', '16', 1),
(41, 6, 'Extra Egg', '', '6', 1),
(42, 6, 'Grilled Halloumi', '', '15', 1),
(43, 6, 'Sauteed Mushrooms', '', '15', 1),
(44, 6, 'Side Salad', '', '10', 1),
(45, 6, 'Smoked Salmon', '', '20', 1),
(46, 7, 'Classic Caesar', 'romaine lettuce, croutons, Parmigiano Reggiano, grilled chicken, fried organic egg, Caesar dressing', '48', 2),
(47, 7, 'Quinoa & Avocado (gf)', ' prawns, iceberg lettuce, pomelo, chilli citrus vinaigrette', '50', 2),
(53, 7, 'Fig & Goat Cheese (gf) ', 'mixed greens, pears, pine nuts, cherry tomatoes, Parmigiano Reggiano, truffle balsamic', '56', 2),
(54, 7, 'Roasted Beetroot Salad (v)(gf)', 'roasted pumpkin, grilled halloumi, chickpeas, baby spinach, sumac dressing', '45', 2),
(55, 7, 'Green Tea Noodles with Smoked Salmon', 'roasted beetroot, sesame seeds, pickled ginger dressing', '48', 2),
(56, 7, 'Wild Rice Salad (v)(gf) ', 'stone fruits, crispy kale, rocket, citrus & ginger dressing', '50', 2),
(57, 7, 'Pantry’s House Salad (v)(gf)', 'mixed greens, radish, shallots, beets, sweet lemon dressing', '40', 2),
(58, 8, 'Mexican Chicken ', 'oregano, paprika, humita sauce, spicy avocado salsa', '42', 2),
(59, 8, 'Roasted Squash Flat Bread (v) ', 'Gorgonzola, crispy kale, pine nuts, chilli oil, pomegranate seeds', '42', 2),
(60, 8, 'Burrata (v)', 'roasted bell peppers, basil oil, crostini', '65', 2),
(61, 8, 'Baked Brie (v)', 'red pepper & tomato chutney, spiced pecan nuts, rosemary, crostini', '56', 2),
(62, 8, 'Kataifi Prawns ', 'lemongrass, galangal, kaffir lime, peanuts, pineapple carpaccio, sweet chilli sauce', '50', 2),
(63, 8, 'Polenta Chips', 'ricotta, Parmigiano Reggiano, rosemary, spiced herb salt', '35', 2),
(64, 9, 'Pantry Breakfast Burger ', 'fried organic egg, beef tomato, turkey ham, aged cheddar, avocado salsa, spicy mayo, brioche bun', '48', 2),
(65, 9, 'Grilled Chicken Burger', 'caramelised onions, aged cheddar, beef tomatoes, gherkins, mustard, spicy mayo, brioche bun', '65', 2),
(66, 9, 'Wagyu Burger', 'caramelised onions, emmental, sautéed mushrooms, rocket,\r\npickles, spicy truffle mayo', '75', 2),
(67, 9, 'brioche bun Tuna Sandwich', 'sweet corn, coriander, chillies, mayo, multi seed baguette', '48', 2),
(68, 9, 'Quinoa Burger (v)', 'mushrooms, peppers, beans, aged cheddar, brioche bun', '55', 2),
(69, 9, 'Barbecue Brisket', 'sriracha, maple syrup, pickles, sourdough baguette', '58', 2),
(70, 9, 'Pulled Chicken Sandwich', 'sun dried tomatoes, basil pesto, aged cheddar, rocket, roasted peppers, rustic bread', '54', 2),
(71, 9, 'Grilled Eggplant Sandwich (v) ', 'sriracha, ricotta, roasted red pepper & tomato chutney, rocket, multi seed bread', '45', 2),
(72, 9, 'Pantry Club Sandwich', 'fried organic egg, grilled chicken, aged cheddar, turkey ham, spicy mayo, toasted brioche', '60', 2),
(73, 10, 'Chicken Tikka Masala', 'raita, flat bread, popadam, salad, quinoa or rice', '75', 3),
(74, 10, 'Shakshouka', ' organic eggs, spicy tomato sauce, jalapeños, feta, pita. Add wagyu meatballs for an additional AED 13', '52', 3),
(75, 10, 'Linguini Aglio e Olio', ' garlic, prawns, capers, crushed chillies, basil', '62', 3),
(76, 10, 'Chilli & Panko Crusted Cream Dory', 'lime & turmeric risotto, grilled asparagus, thyme velouté, chilli oil', '65', 3),
(77, 10, 'Pantry Fish & Chips', 'tartare sauce, house salad', '52', 3),
(78, 10, 'Creamy Taleggio Fettuccine', ' wild mushrooms, baby spinach, grilled chicken, sumac', '65', 3),
(79, 10, 'Slow Roasted Eggplant', 'quinoa, bell peppers, zucchini, basil pesto, bread crumbs, Parmigiano Reggiano, Neapolitan sauce', '52', 3),
(80, 10, 'Wagyu Lasagna', ' bechamel, Parmigiano Reggiano, Neapolitan sauce', '72', 3),
(81, 10, 'Mushroom Risotto', 'forest mushrooms, truffle oil, Parmigiano Reggiano', '54', 3),
(82, 10, 'Beef Brisket ', 'mango salsa, jalapeños, chipotle sour cream, tortilla', '80', 3),
(83, 10, 'Rigatoni Arrabiata (v) ', 'spicy tomato sauce, basil, Parmigiano Reggiano', '48', 3),
(84, 11, 'Tandoori Organic Salmon', 'spinach rice, raita, popadam, chargrilled lemon', '125', 3),
(85, 11, 'Grilled Spatchcock Chicken', 'grilled avocado, roasted red onions, rosemary potatoes', '120', 3),
(86, 12, 'Fries', 'plain or peri-per dusted', '18', 3),
(87, 12, 'Hand-cut Double-Cooked Chips', '', '18', 3),
(88, 12, 'House Salad', '', '10', 3),
(89, 12, 'Sauteed Mushrooms', '', '15', 3),
(90, 12, 'Stir Fried Broccoli ', 'with ginger & sesame', '12', 3),
(91, 12, 'Truffle Parmesan Fries', '', '20', 3),
(92, 12, 'Vegetable Quinoa', '', '20', 3),
(93, 12, ' Spinach Rice', '', '12', 3),
(94, 13, 'Aglio Olio', 'roasted peppers, shrimps, basil, roasted garlic, chilli flakes', '65', 4),
(95, 13, 'Calzone', ' mushrooms, turkey ham, fresh mozzarella, Parmigiano Reggiano, ricotta, tomato sauce', '65', 4),
(96, 13, 'Fiorentina ', 'baby spinach, pine nuts, roasted garlic, chilli oil, goat cheese, tomato sauce', '65', 4),
(97, 13, 'Quattro Formaggi ', 'pecorino, Parmigiano Reggiano, gorgonzola piccante, mozzarella', '65', 4),
(98, 13, 'Tartufo', 'wild mushrooms, rocket, roasted garlic, porcini & truffle cream, brie, Parmigiano Reggiano', '65', 4),
(99, 13, 'Toscana', 'wild mushrooms, black olives, caramelized onions, provolone cheese, tomato sauce', '60', 4),
(100, 13, 'Vegetarian', 'zucchini, aubergine, peppers, black olives, fresh mozzarella, Parmigiano Reggiano, tomato sauce', '60', 4),
(101, 13, 'Spicy Wagyu Meatball', 'calabrian peppers, beef soppressata, rosemary, Parmigiano Reggiano, cream, tomato sauce', '65', 4),
(102, 13, 'Capricciosa', 'artichokes, olives, mushrooms, turkey ham, salami, mozzarella', '65', 4),
(103, 15, 'Home Made Granola', 'with blueberries & warm/cold milk', '15', 5),
(104, 15, 'Organic Egg', ' (cooked any style) with brioche bread', '20', 5),
(105, 15, 'French Toast', ' with nutella, maple syrup, cinnamon, vanilla, brioche bread', '20', 5),
(106, 15, 'Mini Pancakes ', 'with honey, fluffy ricotta', '20', 5),
(107, 15, 'Quinoa Porridge ', 'with milk, strawberries and cream', '20', 5),
(108, 15, 'Fresh Fruits', 'selection of fruits with cream or low-fat yoghurt', '40', 5),
(109, 16, 'Fish ''n Chips', 'with tartare sauce, french fries', '30', 5),
(110, 16, 'Baked Chicken Tenders', 'with french fries', '30', 5),
(111, 16, 'Corn Quesadilla', 'cheddar, chicken, tortilla, thousand island dip', '25', 5),
(112, 16, 'Ratatouille Macaroni', 'hidden veggies, gooey cheese, tomato sauce', '30', 5),
(113, 16, 'Banoffe Pie', 'banana, sticky toffee, crushed digestive biscuits, whipped cream', '25', 5),
(114, 16, 'Kids Pizza', 'mozzarella, tomato sauce, choice of corn, chicken or pepperon', '30', 5),
(115, 16, 'Bangers & Mash', 'chicken sausages, mashed potatoes, brown sauce', '30', 5),
(116, 16, 'Kids Burger', 'wagyu patty, cheddar, ketchup, brioche bun, fries', '35', 5),
(117, 16, 'Crepes ', 'Valrhona dark chocolate, dulcey chocolate, whipped cream', '38', 5),
(118, 17, 'Fresh Fruits', 'selection of fruits with cream or low-fat yoghurt', '40', 6),
(119, 17, 'Banoffe Pie', 'banana, sticky toffee, crushed digestive biscuits, whipped cream', '25', 6),
(120, 17, 'Crepes', 'Valrhona dark chocolate, dulcey chocolate, whipped cream', '38', 6),
(121, 18, 'Cappuccino ', 'espresso, milk, froth', '18', 7),
(122, 18, 'Con Panna', 'double espresso, cream', '20', 7),
(123, 18, 'Dark Mocha', 'espresso, steamed milk, valrhona dark choclate, froth', '20', 7),
(124, 18, 'Dulcey Mocha ', 'espresso, steamed milk, valrhona dulcey choclate, froth', '28', 7),
(125, 18, 'Flat White', 'double espresso, steamed milk, froth', '22', 7),
(126, 18, 'Latte ', 'espresso, steamed milk, froth', '18', 7),
(127, 18, 'Long Black', 'hot water, double espresso', '18', 7),
(128, 18, 'Espresso', 'single shot', '12', 7),
(129, 18, 'Macchiato', 'small cup, double espresso, a touch of froth', '14', 7),
(130, 18, 'Ristretto', 'strong, bold espresso', '12', 7),
(131, 18, 'Piccolo', 'espresso, steamed milk', '16', 7),
(132, 19, 'Caffe Frappe', 'cold brew, milk, ice, vanilla ice-cream', '25', 7),
(133, 19, 'Shakerato ', 'chilled espresso shaken with ice', '25', 7),
(134, 19, 'Iced Cappuccino', 'chilled cold brew espresso, crown of foamed milk', '25', 7),
(135, 6, 'Toffee Coffee', 'caramel toffee blended with cold brew, fresh milk', '25', 7),
(136, 20, 'Mighty Leaf Organic Tea Blends', 'Organic Breakfast, Bombay Chai, Organic Earl Grey, Jasmine Mist, Ginger Twist, Green Tea Passion, Organic Matcha Green Tea, Organic Mint Mélange, Wild Blossoms & Berries', '18', 7),
(137, 20, 'Chai Latte', 'black tea, aromatic spices, frothy milk', '25', 7),
(138, 21, 'The Essential Five', 'blueberries, puffed wheat, banana, almonds, milk', '25', 8),
(139, 21, 'Tropical Kale', 'coconut milk, banana, kale , flax seeds', '25', 8),
(140, 21, 'Mango Lassi', 'mango, yoghurt', '25', 8),
(141, 21, 'Medjool Date', 'medjool dates, banana, milk', '25', 8),
(142, 21, 'Peanut Butter', ' Valrhona chocolate, cocoa, almond milk', '25', 8),
(143, 21, 'Spiced Chai', 'vanilla, cinnamon, ginger, chia seeds, almond milk', '25', 8),
(144, 21, 'Super Seven', 'apple, blueberries, mango, banana, oats, goji berries, yoghurt', '28', 8),
(145, 22, 'Cookies ''n Cream', 'vanilla ice-cream, oreo cookies, milk', '25', 8),
(146, 22, 'Salted Caramel', ' rich dark caramel, vanilla ice-cream, milk', '25', 8),
(147, 22, 'Strawberry Cheesecake', 'cream cheese, strawberry ice-cream, graham crackers, milk', '25', 8),
(148, 22, 'Valrhona Chocolate', 'dark chocolate chips, chocolate ice-cream, cocoa nibs, milk', '25', 8),
(149, 22, 'Frozen Pineapple', ' honey, vanilla ice-cream, milk', '25', 8),
(150, 23, 'Elderflower, cucumber & mint', '', '25', 8),
(151, 23, 'Mixed Berries', '', '25', 8),
(152, 23, ' Lemongrass Cooler ', '', '25', 8),
(153, 24, 'Orange', '', '25', 8),
(154, 24, 'Carrot', '', '30', 8),
(155, 24, ' Watermelon', '', '30', 8),
(156, 24, 'Fresh Coconut Water', '', '25', 8),
(157, 24, 'Mint Lemonade', '', '30', 8),
(158, 24, 'Go Green:', 'kale, apple, ginger, orange', '30', 8),
(159, 24, 'Sunrise:', 'orange, carrot, beetroot', '30', 8),
(160, 25, 'Fentimans Botanically Brewed Beverages ', 'curiosity cola, mandarin & seville orange, rose lemonade, victorian lemonade', '20', 8),
(161, 25, 'James White Fine Pressed Fruit Juice ', 'big tom, organic apple & crushed ginger, beet it shot, organic pear & raspberry', '20', 8);

-- --------------------------------------------------------

--
-- Table structure for table `pcafeapp_ordertrackingtable`
--

CREATE TABLE IF NOT EXISTS `pcafeapp_ordertrackingtable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) NOT NULL,
  `userid` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `item_id` int(11) DEFAULT NULL,
  `extras` varchar(200) NOT NULL,
  `order_date` date NOT NULL,
  `delivery_date` varchar(25) DEFAULT NULL,
  `choosen_items` varchar(100) NOT NULL,
  `cat_id` int(11) DEFAULT NULL,
  `order_type` varchar(30) NOT NULL,
  `sub_cat_id` int(11),
  `recieve_time` time NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=20 ;

--
-- Dumping data for table `pcafeapp_ordertrackingtable`
--

INSERT INTO `pcafeapp_ordertrackingtable` (`id`, `order_id`, `userid`, `quantity`, `price`, `name`, `item_id`, `extras`, `order_date`, `delivery_date`, `choosen_items`, `cat_id`, `order_type`, `sub_cat_id`, `recieve_time`) VALUES
(2, 5525, 20, 4, 160, 'Fresh Fruits (v) (gf)', 1, 'selection of fresh fruits, cream or low-fat yogurt', '2015-07-17', NULL, '', 1, 'yet_to_confirm', 1, '18:08:43'),
(3, 5525, 20, 1, 0, 'Cappuccino ', 121, 'espresso, milk, froth', '2015-07-17', NULL, '', 7, 'yet_to_confirm', 18, '17:51:04'),
(4, 5525, 20, 3, 90, 'Home-Made Granola (v)', 2, 'organic oats, good-for-you seeds, coconut, honey, low-fat\\r\\nyoghurt, Sarabeth''''s preserve or home-made berry compote', '2015-07-17', NULL, '', 1, 'yet_to_confirm', 1, '18:09:36'),
(5, 5525, 20, 2, 96, 'Pantry Breakfast Burger', 8, 'fried organic egg, beef tomato, turkey ham, aged cheddar,\r\navocado salsa, spicy mayo, brioche bun, side salad', '2015-07-17', NULL, '', 1, 'yet_to_confirm', 2, '18:10:53'),
(6, 5525, 20, 2, 104, 'Grilled Portobello Mushrooms (v)', 15, 'spinach, corn, emmental & panko crumbs, Neapolitan sauce', '2015-07-17', NULL, '', 1, 'yet_to_confirm', 3, '18:13:14'),
(7, 5525, 20, 1, 30, 'Spiced Strawberry Bircher Muesli (v)', 4, 'low fat yoghurt, fresh pear, spiced strawberries', '2015-07-17', NULL, '', 1, 'yet_to_confirm', 1, '18:13:21'),
(8, 5525, 20, 1, 25, ' Lemongrass Cooler ', 152, '', '2015-07-17', NULL, '', 8, 'yet_to_confirm', 23, '18:32:39'),
(9, 5525, 5, 1, 40, 'Fresh Fruits (v) (gf)', 1, 'selection of fresh fruits, cream or low-fat yogurt', '2015-07-18', NULL, '', 1, 'yet_to_confirm', 1, '08:38:05'),
(10, 5525, 5, 1, 30, 'Home-Made Granola (v)', 2, 'organic oats, good-for-you seeds, coconut, honey, low-fat\\r\\nyoghurt, Sarabeth''''s preserve or home-made berry compote', '2015-07-18', NULL, '', 1, 'yet_to_confirm', 1, '08:38:05'),
(11, 5525, 5, 1, 40, 'Fresh Fruits (v) (gf)', 1, 'selection of fresh fruits, cream or low-fat yogurt', '2015-07-18', NULL, '', 1, 'yet_to_confirm', 1, '08:40:06'),
(12, 5525, 5, 1, 40, 'Fresh Fruits (v) (gf)', 1, 'selection of fresh fruits, cream or low-fat yogurt', '2015-07-18', NULL, '', 1, 'yet_to_confirm', 1, '08:42:32'),
(13, 7322, 5, 1, 40, 'Fresh Fruits (v) (gf)', 1, 'selection of fresh fruits, cream or low-fat yogurt', '2015-07-18', NULL, '', 1, 'yet_to_confirm', 1, '08:46:02'),
(14, 5504, 5, 1, 30, 'Home-Made Granola (v)', 2, 'organic oats, good-for-you seeds, coconut, honey, low-fat\\r\\nyoghurt, Sarabeth''''s preserve or home-made berry compote', '2015-07-18', NULL, '', 1, 'yet_to_confirm', 1, '08:46:26'),
(15, 5504, 5, 1, 30, 'Quinoa Porridge (v)(gf)', 3, 'chia seeds, coconut milk, goji berries, peaches, toasted coconut', '2015-07-18', NULL, '', 1, 'yet_to_confirm', 1, '08:46:26'),
(16, 3992, 5, 1, 30, 'Quinoa Porridge (v)(gf)', 3, 'chia seeds, coconut milk, goji berries, peaches, toasted coconut', '2015-07-18', NULL, '', 1, 'confirmed', 1, '09:00:19'),
(17, 3992, 5, 2, 60, 'Spiced Strawberry Bircher Muesli (v)', 4, 'low fat yoghurt, fresh pear, spiced strawberries', '2015-07-18', NULL, '', 1, 'confirmed', 1, '09:00:19'),
(18, 4091, 5, 1, 30, 'Spiced Strawberry Bircher Muesli (v)', 4, 'low fat yoghurt, fresh pear, spiced strawberries', '2015-07-18', NULL, '', 1, 'confirmed', 1, '10:04:35'),
(19, 4091, 5, 1, 40, 'Fresh Fruits (v) (gf)', 1, 'selection of fresh fruits, cream or low-fat yogurt', '2015-07-18', NULL, '', 1, 'confirmed', 1, '10:04:35');

-- --------------------------------------------------------

--
-- Table structure for table `pcafeapp_subcategories`
--

CREATE TABLE IF NOT EXISTS `pcafeapp_subcategories` (
  `sub_cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_cat_name` varchar(50) NOT NULL,
  `cat_id_id` int(11) NOT NULL,
  PRIMARY KEY (`sub_cat_id`),
  KEY `pc_cat_id_id_5cc9f4cb70b6e4b3_fk_pcafeapp_categories_category_id` (`cat_id_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=26 ;

--
-- Dumping data for table `pcafeapp_subcategories`
--

INSERT INTO `pcafeapp_subcategories` (`sub_cat_id`, `sub_cat_name`, `cat_id_id`) VALUES
(1, 'FRUITS & GRAINS', 1),
(2, 'BREAKFAST SANDWICHES', 1),
(3, 'MORNING MEALS', 1),
(4, 'ORGANIC EGGS', 1),
(5, 'BREAKFAST SWEETS', 1),
(6, 'BREAKFAST SIDES', 1),
(7, 'SALADS', 2),
(8, 'SHAREABLES', 2),
(9, 'SANDWICHES & BURGERS', 2),
(10, 'MAINS', 3),
(11, 'FROM THE GRILL', 3),
(12, 'SIDES', 3),
(13, 'PIZZA', 4),
(14, 'BYO PIZZA', 4),
(15, 'BREAKFAST', 5),
(16, 'MAINS', 5),
(17, 'DESSERTS', 6),
(18, 'HOT COFFEE', 7),
(19, 'COLD COFFEE', 7),
(20, 'TEA', 7),
(21, 'SMOOTHIES', 8),
(22, 'MILK SHAKES', 8),
(23, 'SPARKLERS', 8),
(24, 'FRESH JUICES', 8),
(25, 'BOTTLED JUICES', 8);

-- --------------------------------------------------------

--
-- Table structure for table `pcafeapp_useraddress`
--

CREATE TABLE IF NOT EXISTS `pcafeapp_useraddress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `area` varchar(50) NOT NULL,
  `po_box` varchar(40) NOT NULL,
  `city` varchar(30) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `is_primary` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `pcafeapp_useraddress`
--

INSERT INTO `pcafeapp_useraddress` (`id`, `userid`, `address`, `area`, `po_box`, `city`, `phone`, `is_primary`) VALUES
(1, 1, 'al safasfdasdf', '20', '', 'Dubai', '', 'True'),
(2, 2, 'al safaasfsadf', '83', '', 'Dubai', '', 'True'),
(3, 3, 'al safaasfsadf', '20', '', 'Dubai', '', 'True'),
(4, 4, 'al safaasfsadf', '20', '', 'Dubai', '', 'True'),
(5, 5, 'al safaasfsadf', '20', '', 'Dubai', '', 'True');

-- --------------------------------------------------------

--
-- Table structure for table `pcafeapp_userdetails`
--

CREATE TABLE IF NOT EXISTS `pcafeapp_userdetails` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(25) NOT NULL,
  `last_name` varchar(25) NOT NULL,
  `password` varchar(50) NOT NULL,
  `phone_no` varchar(25) NOT NULL,
  `email` varchar(50) NOT NULL,
  `dob` varchar(25) NOT NULL,
  `mobile` varchar(30) NOT NULL,
  `how_abt_us` varchar(50) NOT NULL,
  `date_time` datetime NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `company` varchar(50) NOT NULL,
  `verification_code` varchar(10) NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `pcafeapp_userdetails`
--

INSERT INTO `pcafeapp_userdetails` (`userid`, `first_name`, `last_name`, `password`, `phone_no`, `email`, `dob`, `mobile`, `how_abt_us`, `date_time`, `is_active`, `company`, `verification_code`) VALUES
(5, 'Aravind', 'Gajelli', '123456', '789456123', 'aravind.gajellig@gmail.com', '2-1', '9640869487', 'Email', '2015-07-18 08:02:52', 1, '', 'tla291wzs');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `pcafeapp_subcategories`
--
ALTER TABLE `pcafeapp_subcategories`
  ADD CONSTRAINT `pc_cat_id_id_5cc9f4cb70b6e4b3_fk_pcafeapp_categories_category_id` FOREIGN KEY (`cat_id_id`) REFERENCES `pcafeapp_categories` (`category_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
