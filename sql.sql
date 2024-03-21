/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - social_guide
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`social_guide` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `social_guide`;

/*Table structure for table `application` */

DROP TABLE IF EXISTS `application`;

CREATE TABLE `application` (
  `app_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `application` varchar(100) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`app_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `application` */

insert  into `application`(`app_id`,`user_id`,`application`,`date`,`status`,`project_id`) values (1,7,'/static/application/060221-092649.pdf','2021-02-06','forwarded',1),(2,7,'/static/application/060221-164133.pdf','2021-02-06','rejected',1),(3,7,'/static/application/070221-153822.pdf','2021-02-07','pending',1),(4,7,'/static/application/270421-215140.pdf','2021-04-27','pending',1);

/*Table structure for table `assign_work` */

DROP TABLE IF EXISTS `assign_work`;

CREATE TABLE `assign_work` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `clerk_id` int(11) DEFAULT NULL,
  `work` varchar(100) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `assign_work` */

insert  into `assign_work`(`assign_id`,`clerk_id`,`work`,`date`) values (1,5,'jhgfjg','2021-03-30'),(2,5,'likujythh','2021-01-01'),(3,5,'jgfgjf','2021-01-30'),(4,5,'hjhjhj','2021-04-20');

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `A_id` int(11) NOT NULL AUTO_INCREMENT,
  `D_id` int(11) DEFAULT NULL,
  `clerk_id` int(11) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  `attendance` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`A_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `attendance` */

insert  into `attendance`(`A_id`,`D_id`,`clerk_id`,`date`,`attendance`) values (1,4,5,'2021-02-05','Absent'),(2,4,5,'2021-02-07','Present'),(3,4,5,'2021-04-27','Present');

/*Table structure for table `chat_mc` */

DROP TABLE IF EXISTS `chat_mc`;

CREATE TABLE `chat_mc` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `chat_mc` */

insert  into `chat_mc`(`chat_id`,`from_id`,`to_id`,`message`,`date`) values (1,2,3,'kjhgfgh','2021-02-05'),(2,3,2,'lkjhmnbv','2021-02-05'),(3,3,2,'Hi','2021-02-06'),(4,2,3,'jhgldfkgh','2021-02-06'),(5,3,2,'oliukth','2021-02-06'),(6,2,3,'krhgkrjgh','2021-02-07'),(7,2,3,'jgdjh','2021-02-07'),(8,3,2,'mjhfgv','2021-02-07'),(9,2,3,'hghhj','2021-04-27'),(10,2,3,'hlw','2021-04-27'),(11,3,3,'hii','2021-04-27'),(12,3,3,'hii','2021-04-27'),(13,3,3,'hii','2021-04-27'),(14,3,3,'hii','2021-04-27'),(15,3,3,'hii','2021-04-27'),(16,3,3,'hii','2021-04-27'),(17,3,3,'hii','2021-04-27'),(18,3,3,'hii','2021-04-27'),(19,3,3,'hii','2021-04-27'),(20,3,2,'hlwww','2021-04-27'),(21,3,2,'xmxjjm','2021-04-27'),(22,3,7,'hii','2021-04-27'),(23,3,7,'hii','2021-04-27'),(24,7,3,'hlw','2021-04-27');

/*Table structure for table `clerk` */

DROP TABLE IF EXISTS `clerk`;

CREATE TABLE `clerk` (
  `clerk_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  `pin` bigint(30) DEFAULT NULL,
  `district` varchar(30) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `qualification` varchar(30) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  `D_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`clerk_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `clerk` */

insert  into `clerk`(`clerk_id`,`name`,`age`,`gender`,`place`,`post`,`pin`,`district`,`phone`,`email`,`qualification`,`photo`,`D_id`) values (5,'aru',27,'female','kannur','kannur',671312,'Trivandrum',9989887877,'aru@gmail.com','Degree','/static/Photo/210427-171814.jpg',4);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `Comp_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) DEFAULT NULL,
  `Complaint` varchar(500) DEFAULT NULL,
  `Complaint_Date` date DEFAULT NULL,
  `Reply` varchar(500) DEFAULT NULL,
  `Reply_Date` date DEFAULT NULL,
  PRIMARY KEY (`Comp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

/*Table structure for table `corporation` */

DROP TABLE IF EXISTS `corporation`;

CREATE TABLE `corporation` (
  `corp_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `district` varchar(30) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  `no_of_wards` int(11) DEFAULT NULL,
  PRIMARY KEY (`corp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `corporation` */

insert  into `corporation`(`corp_id`,`name`,`place`,`post`,`pin`,`district`,`phone`,`email`,`photo`,`no_of_wards`) values (1,'Kanhangad','kanhangad','kanhangad',679086,'Kasaragod',9876666877,'khd@gmail.com','/static/Photo/210205-170906.jpg',23);

/*Table structure for table `councillor` */

DROP TABLE IF EXISTS `councillor`;

CREATE TABLE `councillor` (
  `co_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_name` varchar(30) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `district` varchar(30) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `qualification` varchar(30) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  `ward` int(11) DEFAULT NULL,
  PRIMARY KEY (`co_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `councillor` */

insert  into `councillor`(`co_id`,`c_name`,`age`,`gender`,`place`,`post`,`pin`,`district`,`phone`,`email`,`qualification`,`photo`,`ward`) values (3,'aaaa',38,'male','kannur','kannur',679086,'Kannur',9876576889,'aa@gmail.com','Degree','/static/Photo/210205-170655.jpg',2),(10,'sreeeee',25,'female','kanhangad','kanhangad',671325,'Kasaragod',987657688,'sreee@gmail.com','Degree','/static/Photo/210209-160324.jpg',6);

/*Table structure for table `councillor_complaint` */

DROP TABLE IF EXISTS `councillor_complaint`;

CREATE TABLE `councillor_complaint` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `councillor_id` int(11) DEFAULT NULL,
  `complaint` varchar(30) DEFAULT NULL,
  `c_date` varchar(30) DEFAULT NULL,
  `reply` varchar(30) DEFAULT NULL,
  `reply_date` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `councillor_complaint` */

insert  into `councillor_complaint`(`c_id`,`councillor_id`,`complaint`,`c_date`,`reply`,`reply_date`) values (1,3,'yfjhg','2021-02-06','ekgrjkqehf','2021-02-07'),(2,3,'jjfhgfhg','2021-02-07','jhjkj','2021-04-27'),(3,3,'hhh','2021-04-27','pending','pending');

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `D_id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`D_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`D_id`,`department`) values (4,'agriculture'),(11,'Revenue');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`f_id`,`user_id`,`feedback`,`date`) values (1,7,'ilkujgfnhjk','2021-02-07'),(2,7,'op;olyitkkdfghj','2021-02-07');

/*Table structure for table `issues` */

DROP TABLE IF EXISTS `issues`;

CREATE TABLE `issues` (
  `issue_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `issues` varchar(100) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`issue_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `issues` */

insert  into `issues`(`issue_id`,`user_id`,`issues`,`date`) values (1,7,'jfhg','2021-02-07'),(2,7,'flood','2021-04-27');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `L_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`L_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`L_id`,`username`,`password`,`type`) values (1,'admin','admin','admin'),(2,'sree@gmail.com','204','mayor'),(3,'aa@gmail.com','702','councillor'),(4,'Agriculture','2170','department'),(5,'aru@gmail.com','4709','clerk'),(6,'kk@gmail.com','5605','clerk'),(7,'ammu@123','1234','user'),(8,'aa@gmail.com','384','deleted'),(9,'Revenue','4620','department'),(10,'sreee@gmail.com','768','deleted'),(11,'Revenue','4686','department'),(12,'k@gmail.com','1302','mayor');

/*Table structure for table `mayor` */

DROP TABLE IF EXISTS `mayor`;

CREATE TABLE `mayor` (
  `mayor_id` int(11) NOT NULL AUTO_INCREMENT,
  `M_name` varchar(30) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `district` varchar(30) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `joining_date` varchar(30) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mayor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `mayor` */

insert  into `mayor`(`mayor_id`,`M_name`,`age`,`gender`,`place`,`post`,`pin`,`district`,`phone`,`email`,`joining_date`,`photo`) values (2,'sreeja',22,'female','kanhangad','kanhangad',671325,'Kasaragod',9876666879,'sree@gmail.com','01/01/2021','/static/Photo/210427-163157.jpg'),(8,'jhgfjhg',34,'female','jdhgf','kanhangad',679086,'Thrissur',9876666877,'aa@gmail.com','01/01/2021','/static/Photo/210207-152922.jpg'),(12,'Kripesh',36,'male','thalassery','temple',670102,'Kannur',8976542310,'k@gmail.com','20-2-2021','/static/Photo/210427-163956.jpg');

/*Table structure for table `mayor_issue` */

DROP TABLE IF EXISTS `mayor_issue`;

CREATE TABLE `mayor_issue` (
  `m_issue_id` int(11) NOT NULL AUTO_INCREMENT,
  `councillor_id` int(11) DEFAULT NULL,
  `issue` varchar(30) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`m_issue_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `mayor_issue` */

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `N_id` int(11) NOT NULL AUTO_INCREMENT,
  `clerk_id` int(11) DEFAULT NULL,
  `notification` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`N_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`N_id`,`clerk_id`,`notification`,`date`) values (1,5,'ghfhgf','2021-02-07');

/*Table structure for table `project` */

DROP TABLE IF EXISTS `project`;

CREATE TABLE `project` (
  `project_id` int(11) NOT NULL AUTO_INCREMENT,
  `councillor_id` int(11) DEFAULT NULL,
  `project` varchar(100) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `project` */

insert  into `project`(`project_id`,`councillor_id`,`project`,`date`,`status`) values (1,3,'water','2021-02-05','approved'),(2,3,'ytgfgd','2021-02-07','pending');

/*Table structure for table `project_timing` */

DROP TABLE IF EXISTS `project_timing`;

CREATE TABLE `project_timing` (
  `pt_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `timeperiod` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`pt_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `project_timing` */

insert  into `project_timing`(`pt_id`,`project_id`,`timeperiod`) values (1,1,'2021-04-02'),(2,1,'2021-04-07');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  `rating` varchar(30) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`user_id`,`dept_id`,`rating`,`date`) values (1,7,4,'3','2021-02-07'),(2,7,4,'4','2021-04-27');

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  `clerk_id` int(11) DEFAULT NULL,
  `report` varchar(100) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `report` */

insert  into `report`(`report_id`,`clerk_id`,`report`,`date`) values (1,5,'k,jgjhgf','2021-02-07');

/*Table structure for table `suggestion` */

DROP TABLE IF EXISTS `suggestion`;

CREATE TABLE `suggestion` (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `councillor_id` int(11) DEFAULT NULL,
  `suggestion` varchar(100) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `suggestion` */

insert  into `suggestion`(`s_id`,`councillor_id`,`suggestion`,`date`) values (1,3,'jhgfdgfdhf','2021-02-07');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(30) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `district` varchar(30) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `ward` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`user_name`,`age`,`gender`,`place`,`post`,`pin`,`district`,`phone`,`email`,`ward`) values (7,'Ammu',34,'Female','kasaragod','Kasaragod',671319,'Kasaragod',9078654321,'ammu@gmail.com',6);

/*Table structure for table `user_complaint` */

DROP TABLE IF EXISTS `user_complaint`;

CREATE TABLE `user_complaint` (
  `comp_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `c_date` varchar(30) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `reply_date` varchar(30) DEFAULT NULL,
  `D_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`comp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user_complaint` */

insert  into `user_complaint`(`comp_id`,`user_id`,`complaint`,`c_date`,`reply`,`reply_date`,`D_id`) values (1,7,'hgfhgf','2021-02-07','pending','pending',4),(2,7,'hdghjh','2021-04-27','pending','pending',4);

/*Table structure for table `work` */

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `Work_id` int(11) NOT NULL AUTO_INCREMENT,
  `Clerk_id` int(11) DEFAULT NULL,
  `Work` varchar(100) DEFAULT NULL,
  `Work_date` date DEFAULT NULL,
  PRIMARY KEY (`Work_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `work` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
