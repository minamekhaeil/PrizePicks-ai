import datetime,json,pathlib,urllib.request
now=datetime.datetime.now(datetime.timezone.utc)
date=now.astimezone(datetime.timezone(datetime.timedelta(hours=-4))).strftime('%Y%m%d')
output={'updated_at':now.isoformat(),'schedule_status':'unavailable','props_status':'unavailable — no verified provider','games':[]}
try:
 req=urllib.request.Request('https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates='+date,headers={'User-Agent':'NBA-Prop-Research-Lab/1.0'})
 with urllib.request.urlopen(req,timeout=20) as response: data=json.load(response)
 for event in data.get('events',[]):
  comp=(event.get('competitions') or [{}])[0]
  teams={t.get('homeAway'):t.get('team',{}).get('displayName','Unknown') for t in comp.get('competitors',[])}
  output['games'].append({'home':teams.get('home','Unknown'),'away':teams.get('away','Unknown'),'status':event.get('status',{}).get('type',{}).get('description','Scheduled')})
 output['schedule_status']='available via ESPN public scoreboard'
except Exception as e: output['schedule_status']='fetch failed: '+type(e).__name__
path=pathlib.Path('data/latest.json');path.parent.mkdir(exist_ok=True);path.write_text(json.dumps(output,indent=2)+'\n')
