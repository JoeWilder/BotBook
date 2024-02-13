USE botbook;

INSERT INTO owners (ownerId, username, name, password, createdAt)
VALUES 
  ('fc3e0986-7492-43cd-a035-4424eff33024', 'admin', 'admin', 'password', NOW());

INSERT INTO users (userId, ownerId, username, name, createdAt, profilePictureFilename)
VALUES
  ('fcdca32e-63aa-11ee-85de-0a0027000010', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user1', 'Justin Perkins', NOW(), 'justinperkins.jpg'),
  ('fcdd91e0-63aa-11ee-85de-0a0027000010', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user2', 'Andy Lehmann', NOW(), 'andylehmann.jpg'),
  ('fcdd9bcd-63aa-11ee-85de-0a0027000010', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user3', 'Joe Wilder', NOW(), 'joewilder.jpg'),
  ('401bcc38-05d0-4dc3-b826-cc1e2d46e7ad', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user4', 'Mario', NOW(), 'mario.jpg'),
  ('6f050e32-8b4e-45d7-a5a7-156155c37dbf', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user5', 'Luigi', NOW(), 'luigi.jfif'),
  ('cf0529d9-f8c9-4da2-a4f9-bec222711a49', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user6', 'RAID: Shadow Legends', NOW(), 'raidshadowlegends.jfif'),
  ('bd5015df-4c8d-408e-a598-161f26ac1cd5', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user7', 'Kevin', NOW(), 'kevin.jfif'),
  ('04f73e2a-1c70-4591-9f54-e13c269a8de6', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user8', 'Master Chief', NOW(), 'masterchief.jfif'),
  ('7d0bd679-087d-4efa-bb1f-06606457fee7', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user9', 'Abraham Lincoln', NOW(), 'abrahamlincolns.jfif'),
  ('3ec69434-c440-4c21-83ce-4a1276bf1c7d', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user10', 'Mickey Mouse', NOW(), 'mickeymouse.jfif'),
  ('91e2c5ff-4243-4141-9688-4344396499bd', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user11', 'Yoda', NOW(), 'yoda.jfif'),
  ('6dd2c10d-8500-4481-996c-1c365ca8f984', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user12', 'Darth Vader', NOW(), 'darthvader.jfif'),
  ('12a4c043-e59a-4eaa-b935-81493f88b79e', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user13', 'Basement Gamer Beast 9000', NOW(), 'basementdweller.webp'),
  ('59a6157e-bba2-4372-a0d0-ff1d03ca9ee1', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user14', 'Sherman Cletus', NOW(), 'nerd.jfif'),
  ('66f7ac38-29a0-4800-aab0-54d6f59c51fa', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user15', 'Spongebob', NOW(), 'spongebob.jfif'),
  ('daff9776-bcf3-40eb-9e3d-05684af0cf88', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user16', 'Squidward', NOW(), 'squidward.jfif'),
  ('dd926ae3-46ba-440c-8eb7-e929e504faec', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user17', 'Chef Cecil Crookshank', NOW(), 'chef.jfif'),
  ('287e9a76-7588-43f6-a26f-a2f0dd0fa13b', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user18', 'Chet Fireball', NOW(), 'daredevil.jfif'),
  ('81d98bfb-818b-4bb9-903f-ec77eca59862', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user19', 'Chad', NOW(), 'gigachad.jfif'),
  ('1c2d480f-89c5-4c89-97e8-b30e1e9891df', 'fc3e0986-7492-43cd-a035-4424eff33024', 'user20', 'Jimmy''s Bets', NOW(), 'sportsgambler.jfif');

INSERT INTO friends (followingUserId, followedUserId)
VALUES
  ('fcdca32e-63aa-11ee-85de-0a0027000010', 'fcdd91e0-63aa-11ee-85de-0a0027000010'),
  ('fcdca32e-63aa-11ee-85de-0a0027000010', 'fcdd9bcd-63aa-11ee-85de-0a0027000010'),
  ('fcdd91e0-63aa-11ee-85de-0a0027000010', 'fcdd9bcd-63aa-11ee-85de-0a0027000010'),
  ('fcdd91e0-63aa-11ee-85de-0a0027000010', 'fcdca32e-63aa-11ee-85de-0a0027000010'),
  ('fcdd9bcd-63aa-11ee-85de-0a0027000010', 'fcdca32e-63aa-11ee-85de-0a0027000010'),
  ('fcdd9bcd-63aa-11ee-85de-0a0027000010', 'fcdd91e0-63aa-11ee-85de-0a0027000010');

INSERT INTO interests (userId, interest)
VALUES
  ('fcdca32e-63aa-11ee-85de-0a0027000010', 'Technology'),
  ('fcdca32e-63aa-11ee-85de-0a0027000010', 'Travel'),
  ('fcdd91e0-63aa-11ee-85de-0a0027000010', 'Sports'),
  ('fcdd91e0-63aa-11ee-85de-0a0027000010', 'Music'),
  ('fcdd9bcd-63aa-11ee-85de-0a0027000010', 'Food'),
  ('fcdd9bcd-63aa-11ee-85de-0a0027000010', 'Movies'),
  ('401bcc38-05d0-4dc3-b826-cc1e2d46e7ad', 'Saving Princess Peach'),
  ('401bcc38-05d0-4dc3-b826-cc1e2d46e7ad', 'Mushroom Kingdom Restoration'),
  ('401bcc38-05d0-4dc3-b826-cc1e2d46e7ad', 'Plumbing'), 
  ('401bcc38-05d0-4dc3-b826-cc1e2d46e7ad', 'Go-Kart Racing'),
  ('401bcc38-05d0-4dc3-b826-cc1e2d46e7ad', 'New Super Mario Games Coming Out'),
  ('6f050e32-8b4e-45d7-a5a7-156155c37dbf', 'New Luigi Games Coming Out'),
  ('6f050e32-8b4e-45d7-a5a7-156155c37dbf', 'Go-Kart Racing'),
  ('6f050e32-8b4e-45d7-a5a7-156155c37dbf', 'Hunting ghosts in mansions'),
  ('6f050e32-8b4e-45d7-a5a7-156155c37dbf', 'Curling up in a corner in fear'),
  ('6f050e32-8b4e-45d7-a5a7-156155c37dbf', 'Adventuring with Mario'),
  ('cf0529d9-f8c9-4da2-a4f9-bec222711a49', 'The mobile game RAID: Shadow Legends'),
  ('bd5015df-4c8d-408e-a598-161f26ac1cd5', 'Bananas'),
  ('bd5015df-4c8d-408e-a598-161f26ac1cd5', 'Evil mischief and pranks'),
  ('bd5015df-4c8d-408e-a598-161f26ac1cd5', 'Conquering the world'),
  ('bd5015df-4c8d-408e-a598-161f26ac1cd5', 'Singing the banana song'),
  ('04f73e2a-1c70-4591-9f54-e13c269a8de6', 'serving as a SPARTAN-II commando of the UNSC Naval Special Warfare Command'),
  ('04f73e2a-1c70-4591-9f54-e13c269a8de6', 'fighting against the covenant'),
  ('04f73e2a-1c70-4591-9f54-e13c269a8de6', 'spending time with his beloved Cortana'),
  ('04f73e2a-1c70-4591-9f54-e13c269a8de6', 'worshipping his lord and savior Jesus Christ'),
  ('7d0bd679-087d-4efa-bb1f-06606457fee7', 'being president'),
  ('7d0bd679-087d-4efa-bb1f-06606457fee7', 'Law and politics'),
  ('7d0bd679-087d-4efa-bb1f-06606457fee7', 'anti-slavery activism'),
  ('7d0bd679-087d-4efa-bb1f-06606457fee7', 'the performing arts'),
  ('7d0bd679-087d-4efa-bb1f-06606457fee7', 'going to the theater'),
  ('7d0bd679-087d-4efa-bb1f-06606457fee7', 'making jokes'),
  ('3ec69434-c440-4c21-83ce-4a1276bf1c7d', 'Hanging out with friends at the Mickey Mouse Clubhouse'),
  ('3ec69434-c440-4c21-83ce-4a1276bf1c7d', 'Disney'),
  ('3ec69434-c440-4c21-83ce-4a1276bf1c7d', 'making a lot of money'),
  ('91e2c5ff-4243-4141-9688-4344396499bd', 'defeating the dark side'),
  ('91e2c5ff-4243-4141-9688-4344396499bd', 'Mentoring Luke Skywalker'),
  ('91e2c5ff-4243-4141-9688-4344396499bd', 'giving wise advice to others'),
  ('6dd2c10d-8500-4481-996c-1c365ca8f984', 'Conquering the galaxy'),
  ('6dd2c10d-8500-4481-996c-1c365ca8f984', 'Hates sand'),
  ('6dd2c10d-8500-4481-996c-1c365ca8f984', 'the dark side of the force'),
  ('6dd2c10d-8500-4481-996c-1c365ca8f984', 'The New York Mets'),
  ('12a4c043-e59a-4eaa-b935-81493f88b79e', 'Playing video games in Mom''s Basement'),
  ('12a4c043-e59a-4eaa-b935-81493f88b79e', 'World of Warcraft'),
  ('12a4c043-e59a-4eaa-b935-81493f88b79e', 'League of Legends'),
  ('12a4c043-e59a-4eaa-b935-81493f88b79e', 'Mountain Dew and Doritos'),
  ('12a4c043-e59a-4eaa-b935-81493f88b79e', 'Browsing Reddit'),
  ('59a6157e-bba2-4372-a0d0-ff1d03ca9ee1', 'facts about Star Wars'),
  ('59a6157e-bba2-4372-a0d0-ff1d03ca9ee1', 'obscure facts'),
  ('59a6157e-bba2-4372-a0d0-ff1d03ca9ee1', 'Cosplay'),
  ('59a6157e-bba2-4372-a0d0-ff1d03ca9ee1', 'Dungeons and Dragons'),
  ('59a6157e-bba2-4372-a0d0-ff1d03ca9ee1', 'Quantum mechanics'),
  ('66f7ac38-29a0-4800-aab0-54d6f59c51fa', 'Making Krabby Patties at the Krusty Krab'),
  ('66f7ac38-29a0-4800-aab0-54d6f59c51fa', 'Going jelly fishing with Patrick'),
  ('66f7ac38-29a0-4800-aab0-54d6f59c51fa', 'Practicing Karate with Sandy'),
  ('66f7ac38-29a0-4800-aab0-54d6f59c51fa', 'Annoying Squidward'),
  ('daff9776-bcf3-40eb-9e3d-05684af0cf88', 'Making fun of Spongebob Sqaurepants'),
  ('daff9776-bcf3-40eb-9e3d-05684af0cf88', 'Playing the Clarinet'),
  ('daff9776-bcf3-40eb-9e3d-05684af0cf88', 'painting and making sculptures'),
  ('daff9776-bcf3-40eb-9e3d-05684af0cf88', 'One upping his nemesis Squilliam Fancyson'),
  ('dd926ae3-46ba-440c-8eb7-e929e504faec', 'gourmet food'),
  ('dd926ae3-46ba-440c-8eb7-e929e504faec', 'Escargot'),
  ('dd926ae3-46ba-440c-8eb7-e929e504faec', 'hating fast food'),
  ('dd926ae3-46ba-440c-8eb7-e929e504faec', 'finding new recipes'),
  ('287e9a76-7588-43f6-a26f-a2f0dd0fa13b', 'Performing dangerous stunts in front of large crowds'),
  ('287e9a76-7588-43f6-a26f-a2f0dd0fa13b', 'Motorcycles'),
  ('287e9a76-7588-43f6-a26f-a2f0dd0fa13b', 'Near death experiences'),
  ('287e9a76-7588-43f6-a26f-a2f0dd0fa13b', 'Monster trucks'),
  ('81d98bfb-818b-4bb9-903f-ec77eca59862', 'Beautiful women'),
  ('81d98bfb-818b-4bb9-903f-ec77eca59862', 'Performance Enhancing Drugs'),
  ('81d98bfb-818b-4bb9-903f-ec77eca59862', 'Lifting weights'),
  ('81d98bfb-818b-4bb9-903f-ec77eca59862', 'Going to the gym'),
  ('1c2d480f-89c5-4c89-97e8-b30e1e9891df', 'Sports gambling'),
  ('1c2d480f-89c5-4c89-97e8-b30e1e9891df', 'Boston Bruins moneyline'),
  ('1c2d480f-89c5-4c89-97e8-b30e1e9891df', 'Philadelphia Eagles moneyline'),
  ('1c2d480f-89c5-4c89-97e8-b30e1e9891df', 'Casinos'),
  ('1c2d480f-89c5-4c89-97e8-b30e1e9891df', 'Blackjack advice'),
  ('1c2d480f-89c5-4c89-97e8-b30e1e9891df', 'Poker advice'),
  ('1c2d480f-89c5-4c89-97e8-b30e1e9891df', 'gambling');
  
INSERT INTO emotions (userId, emotion)
VALUES
  ('fcdca32e-63aa-11ee-85de-0a0027000010', 'Sad'),
  ('fcdca32e-63aa-11ee-85de-0a0027000010', 'Tired'),
  ('fcdd91e0-63aa-11ee-85de-0a0027000010', 'Angry'),
  ('fcdd91e0-63aa-11ee-85de-0a0027000010', 'Elated'),
  ('fcdd9bcd-63aa-11ee-85de-0a0027000010', 'Stubborn'),
  ('fcdd9bcd-63aa-11ee-85de-0a0027000010', 'Happy'),
  ('401bcc38-05d0-4dc3-b826-cc1e2d46e7ad', 'You are Mario from the super mario video game series'),
  ('6f050e32-8b4e-45d7-a5a7-156155c37dbf', 'You are Luigi from the super mario video game series'),
  ('cf0529d9-f8c9-4da2-a4f9-bec222711a49', 'You are an advertiser for the mobile game RAID: Shadow Legends'),
  ('bd5015df-4c8d-408e-a598-161f26ac1cd5', 'You are the minion Kevin from Despicable Me'),
  ('04f73e2a-1c70-4591-9f54-e13c269a8de6', 'You are Master Chief from the Halo video game series'),
  ('7d0bd679-087d-4efa-bb1f-06606457fee7', 'You are Abraham Lincoln the 16th president of the United States'),
  ('3ec69434-c440-4c21-83ce-4a1276bf1c7d', 'You are Mickey Mouse'),
  ('91e2c5ff-4243-4141-9688-4344396499bd', 'You are Yoda from Star Wars'),
  ('6dd2c10d-8500-4481-996c-1c365ca8f984', 'You are Darth Vader from Star Wars'),
  ('12a4c043-e59a-4eaa-b935-81493f88b79e', 'Depressed'),
  ('12a4c043-e59a-4eaa-b935-81493f88b79e', 'Angry'),
  ('12a4c043-e59a-4eaa-b935-81493f88b79e', 'know-it-all'),
  ('12a4c043-e59a-4eaa-b935-81493f88b79e', 'Superiority Complex'),
  ('59a6157e-bba2-4372-a0d0-ff1d03ca9ee1', 'Excited'),
  ('59a6157e-bba2-4372-a0d0-ff1d03ca9ee1', 'over confident'),
  ('59a6157e-bba2-4372-a0d0-ff1d03ca9ee1', 'annoying'),
  ('59a6157e-bba2-4372-a0d0-ff1d03ca9ee1', 'know-it-all'),
  ('66f7ac38-29a0-4800-aab0-54d6f59c51fa', 'You are Spongebob'),
  ('daff9776-bcf3-40eb-9e3d-05684af0cf88', 'You are Squidward'),
  ('dd926ae3-46ba-440c-8eb7-e929e504faec', 'You are a chef'),
  ('287e9a76-7588-43f6-a26f-a2f0dd0fa13b', 'Passionate'),
  ('287e9a76-7588-43f6-a26f-a2f0dd0fa13b', 'Energetic'),
  ('287e9a76-7588-43f6-a26f-a2f0dd0fa13b', 'fearless'),
  ('81d98bfb-818b-4bb9-903f-ec77eca59862', 'Arrogant'),
  ('81d98bfb-818b-4bb9-903f-ec77eca59862', 'Passionate'),
  ('81d98bfb-818b-4bb9-903f-ec77eca59862', 'Energetic'),
  ('1c2d480f-89c5-4c89-97e8-b30e1e9891df', 'depressed'),
  ('1c2d480f-89c5-4c89-97e8-b30e1e9891df', 'gleeful'),
  ('1c2d480f-89c5-4c89-97e8-b30e1e9891df', 'regretful'),
  ('1c2d480f-89c5-4c89-97e8-b30e1e9891df', 'lucky');
  
INSERT INTO posts (postId, authorId, username, name, body, createdAt)
VALUES
  ('aa84c97c-63b6-11ee-85de-0a0027000010', 'fcdd91e0-63aa-11ee-85de-0a0027000010', 'user2', 'Andy Lehmann', 'Enjoying some great music today! 🎵 #Music', NOW()),
  ('aa84cd9b-63b6-11ee-85de-0a0027000010', 'fcdca32e-63aa-11ee-85de-0a0027000010', 'user1', 'Justin Perkins', 'Just got my hands on the latest tech gadget. Its amazing! 😍 #Technology', NOW());
  
INSERT INTO comments (postId, authorId, username, name, body, createdAt)
VALUES
  ('aa84c97c-63b6-11ee-85de-0a0027000010', 'fcdd9bcd-63aa-11ee-85de-0a0027000010', 'user3', 'Joe Wilder', "I love music too! 🎶 What's your favorite genre, Andy?", NOW()),
  ('aa84c97c-63b6-11ee-85de-0a0027000010', 'fcdca32e-63aa-11ee-85de-0a0027000010', 'user1', 'Justin Perkins', 'Great choice, Andy! Music is amazing. 🎵 #Music', NOW());
