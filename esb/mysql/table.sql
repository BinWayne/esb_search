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

--trade_code和trade_name可为空吗？？
CREATE TABLE IF NOT EXISTS esbdata_services(
   id INT UNSIGNED AUTO_INCREMENT,
   bigCategory VARCHAR(10) NOT NULL,
   subCategory VARCHAR(10) NOT NULL,
   svcCode CHAR(20) NOT NULL,
   svcName VARCHAR(40) NOT NULL,
   sceneCode CHAR(10) NOT NULL,
   sceneName VARCHAR(40) NOT NULL,
   tradeCode VARCHAR(40),
   tradeName VARCHAR(40),
   consumer VARCHAR(20) NOT NULL,
   provider VARCHAR(20) NOT NULL,
   status VARCHAR(10) NOT NULL,
   PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE esbdata_services ADD UNIQUE KEY(svcCode, sceneCode,tradeCode,consumer,provider);

--服务码+场景码+消费方+服务方+交易码  唯一约束？
