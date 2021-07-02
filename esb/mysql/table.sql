-- esb.overview definition

CREATE TABLE esb.overview (
  `big_category` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `sub_category` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `svc_code` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `svc_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `scene_code` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `scene_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `trade_code` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `trade_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `consumer` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `provider` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `status` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `id` INT UNSIGNED AUTO_INCREMENT,
  PRIMARY KEY ( `id` )
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;