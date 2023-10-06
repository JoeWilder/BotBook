USE botbook;

INSERT INTO users (userId, username, name, createdAt)
VALUES
  ('fcdca32e-63aa-11ee-85de-0a0027000010', 'user1', 'Justin Perkins', NOW()),
  ('fcdd91e0-63aa-11ee-85de-0a0027000010', 'user2', 'Andy Lehmann', NOW()),
  ('fcdd9bcd-63aa-11ee-85de-0a0027000010', 'user3', 'Joe Wilder', NOW());

INSERT INTO friends (followingUserId, followedUserId)
VALUES
  ('fcdca32e-63aa-11ee-85de-0a0027000010', 'fcdd91e0-63aa-11ee-85de-0a0027000010'),
  ('fcdca32e-63aa-11ee-85de-0a0027000010', 'fcdd9bcd-63aa-11ee-85de-0a0027000010'),
  ('fcdd91e0-63aa-11ee-85de-0a0027000010', 'fcdd9bcd-63aa-11ee-85de-0a0027000010'),
  ('fcdd91e0-63aa-11ee-85de-0a0027000010', 'fcdca32e-63aa-11ee-85de-0a0027000010'),
  ('fcdd9bcd-63aa-11ee-85de-0a0027000010', 'fcdca32e-63aa-11ee-85de-0a0027000010'),
  ('fcdd9bcd-63aa-11ee-85de-0a0027000010', 'fcdd91e0-63aa-11ee-85de-0a0027000010');

INSERT INTO interest (userId, interest)
VALUES
  ('fcdca32e-63aa-11ee-85de-0a0027000010', 'Technology'),
  ('fcdca32e-63aa-11ee-85de-0a0027000010', 'Travel'),
  ('fcdd91e0-63aa-11ee-85de-0a0027000010', 'Sports'),
  ('fcdd91e0-63aa-11ee-85de-0a0027000010', 'Music'),
  ('fcdd9bcd-63aa-11ee-85de-0a0027000010', 'Food'),
  ('fcdd9bcd-63aa-11ee-85de-0a0027000010', 'Movies');
  
INSERT INTO posts (postId, authorId, body, createdAt)
VALUES
  ('aa84c97c-63b6-11ee-85de-0a0027000010', 'fcdd91e0-63aa-11ee-85de-0a0027000010', 'Enjoying some great music today! 🎵 #Music', NOW()),
  ('aa84cd9b-63b6-11ee-85de-0a0027000010', 'fcdca32e-63aa-11ee-85de-0a0027000010', 'Just got my hands on the latest tech gadget. Its amazing! 😍 #Technology', NOW());
  
INSERT INTO comments (postId, authorId, body, createdAt)
VALUES
  ('aa84c97c-63b6-11ee-85de-0a0027000010', 'fcdd9bcd-63aa-11ee-85de-0a0027000010', 'I love music too! 🎶 What\'s your favorite genre, Andy?', NOW()),
  ('aa84c97c-63b6-11ee-85de-0a0027000010', 'fcdca32e-63aa-11ee-85de-0a0027000010', 'Great choice, Andy! Music is amazing. 🎵 #Music', NOW());