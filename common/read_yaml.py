import logging

import yaml

logging.info("开始读取yaml")
with open("config/config.yaml" , "r", encoding="utf-8") as f:
    url = yaml.safe_load(f)#读取生成字典

    base_url= url['url']
    login_url = base_url+ url["login_url"]
    device_model_url = base_url+url["device_model_url"]
    service_rule_url = base_url+url["service_rule_url"]
