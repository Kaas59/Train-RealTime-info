import requests
import os
import json
from sqlalchemy import create_engine, text

def mysql_connector():
  return create_engine("mysql://root:root@mysql/train?charset=utf8")

def api_request():
  url = os.environ['tokyo-open-data-challenge-url'] + "odpt:Train" + "?odpt:operator=odpt.Operator:JR-East" + "&acl:consumerKey=" + os.environ['tokyo-open-data-challenge-token']
  res = requests.get(url)
  res = json.loads(res.content)
  print("取得件数："+ str(len(res)))
  return res

def mysql_insert(engine, res):
  for value in res:
    if value['odpt:railway'] == "odpt.Railway:JR-East.ChuoRapid":
      q = text("INSERT INFO train_log (train_id, odpt_type, dc_date, dct_valid, odpt_delay, odpt_railway, odpt_operator, odpt_train_number, odpt_train_type, odpt_toStation, odpt_from_station, odpt_rail_direction, odpt_car_composition, odpt_destination_station) VALUES (%s, %s, %s, %s, %d, %s, %s, %s, %s, %s, %s, %s, %d, %s);" % (value['@id'], value['@type'], value['dc:date'], value['dct:valid'], value['odpt:delay'], value['odpt:railway'], value['odpt:operator'], value['odpt_train_number'], value['odpt_train_type'], value['odpt_toStation'], value['odpt_from_station'], value['odpt_rail_direction'], value['odpt_car_composition'], value['odpt_destination_station']))
      rs = engine.execute(q)
      print(rs)

def main():
  engine = mysql_connector()
  res = api_request()
  mysql_insert(engine, res)

if __name__ == '__main__':
  main()
