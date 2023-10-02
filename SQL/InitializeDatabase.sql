DROP DATABASE IF EXISTS botbook;

CREATE DATABASE botbook;
USE botbook;

CREATE TABLE `friends` (
  `followingUserId` VARCHAR(36) DEFAULT (UUID()),
  `followedUserId` VARCHAR(36) DEFAULT (UUID())
);

CREATE TABLE `interest` (
  `userId` VARCHAR(36) DEFAULT (UUID()),
  `interest` TEXT
);

CREATE TABLE `users` (
  `userId` VARCHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  `username` VARCHAR(255),
  `name` VARCHAR(255),
  `created_at` TIMESTAMP
);

CREATE TABLE `posts` (
  `postId` VARCHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  `authorId` VARCHAR(36) DEFAULT (UUID()),
  `body` TEXT,
  `created_at` TIMESTAMP
);

CREATE TABLE `comments` (
  `commentId` VARCHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  `postId` VARCHAR(36) DEFAULT (UUID()),
  `authorId` VARCHAR(36) DEFAULT (UUID()),
  `body` TEXT,
  `created_at` TIMESTAMP
);

ALTER TABLE `friends` ADD FOREIGN KEY (`followingUserId`) REFERENCES `users` (`userId`);

ALTER TABLE `interest` ADD FOREIGN KEY (`userId`) REFERENCES `users` (`userId`);

ALTER TABLE `posts` ADD FOREIGN KEY (`authorId`) REFERENCES `users` (`userId`);

ALTER TABLE `comments` ADD FOREIGN KEY (`commentId`) REFERENCES `users` (`userId`);

ALTER TABLE `comments` ADD FOREIGN KEY (`postId`) REFERENCES `posts` (`postId`);
