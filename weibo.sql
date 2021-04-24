CREATE TABLE `weibo` (
  `id` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `bid` varchar(12) COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_id` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `screen_name` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `text` varchar(2000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `article_url` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `topics` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `at_users` varchar(1000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `pics` varchar(3000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `video_url` varchar(1000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `location` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `source` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `attitudes_count` int(11) DEFAULT NULL,
  `comments_count` int(11) DEFAULT NULL,
  `reposts_count` int(11) DEFAULT NULL,
  `retweet_id` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `keyword` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;