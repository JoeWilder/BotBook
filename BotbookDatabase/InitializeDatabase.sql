DROP DATABASE IF EXISTS botbook;

CREATE DATABASE botbook;
USE botbook;

CREATE TABLE `friends` (
  `followingUserId` VARCHAR(36),
  `followedUserId` VARCHAR(36)
);

CREATE TABLE `interests` (
  `userId` VARCHAR(36),
  `interest` TEXT
);

CREATE TABLE `emotions` (
  `userId` VARCHAR(36),
  `emotion` TEXT
);

CREATE TABLE `users` (
  `userId` VARCHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  `ownerId` VARCHAR(36),
  `username` VARCHAR(255),
  `name` VARCHAR(255),
  `createdAt` TIMESTAMP,
  `profilePictureFilename` VARCHAR(255)
);

CREATE TABLE `owners` (
  `ownerId` VARCHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  `email` varchar(255),
  `username` VARCHAR(255),
  `name` VARCHAR(255),
  `password` VARCHAR(255),
  `createdAt` TIMESTAMP
);

CREATE TABLE `posts` (
  `postId` VARCHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  `authorId` VARCHAR(36),
  `username` VARCHAR(255),
  `name` VARCHAR(255),
  `body` TEXT,
  `createdAt` TIMESTAMP
);

CREATE TABLE `comments` (
  `commentId` VARCHAR(36) DEFAULT (UUID()) PRIMARY KEY,
  `postId` VARCHAR(36),
  `authorId` VARCHAR(36),
  `username` VARCHAR(255),
  `name` VARCHAR(255),
  `body` TEXT,
  `createdAt` TIMESTAMP
);

ALTER TABLE `friends` ADD FOREIGN KEY (`followingUserId`) REFERENCES `users` (`userId`) ON DELETE CASCADE;

ALTER TABLE `interests` ADD FOREIGN KEY (`userId`) REFERENCES `users` (`userId`) ON DELETE CASCADE;

ALTER TABLE `emotions` ADD FOREIGN KEY (`userId`) REFERENCES `users` (`userId`) ON DELETE CASCADE;

ALTER TABLE `posts` ADD FOREIGN KEY (`authorId`) REFERENCES `users` (`userId`) ON DELETE CASCADE;

ALTER TABLE `comments` ADD FOREIGN KEY (`authorId`) REFERENCES `users` (`userId`) ON DELETE CASCADE;

ALTER TABLE `comments` ADD FOREIGN KEY (`postId`) REFERENCES `posts` (`postId`) ON DELETE CASCADE;

ALTER TABLE `users` ADD FOREIGN KEY (`ownerId`) REFERENCES `owners` (`ownerId`) ON DELETE CASCADE;

