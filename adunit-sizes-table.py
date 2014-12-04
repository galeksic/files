Z = [{
    'w': 210,
    'h': 310,
    'f': "MY AD UNIT"
}, {
    'w': 120,
    'h': 240,
    'f': "vertical banner"
}, {
    'w': 120,
    'h': 600,
    'f': "skyscraper"
}, {
    'w': 125,
    'h': 125,
    'f': "button"
}, {
    'w': 160,
    'h': 600,
    'f': "wide skyscraper"
}, {
    'w': 180,
    'h': 150,
    'f': "small rectangle"
}, {
    'w': 200,
    'h': 200,
    'f': "small square"
}, {
    'w': 234,
    'h': 60,
    'f': "half banner"
}, {
    'w': 250,
    'h': 250,
    'f': "square"
}, {
    'w': 300,
    'h': 250,
    'f': "medium rectangle"
}, {
    'w': 300,
    'h': 600,
    'f': "half page"
}, {
    'w': 320,
    'h': 50,
    'f': "mobile leaderboard"
},  {
    'w': 320,
    'h': 100,
    'f': "large mobile banner"
}, {
    'w': 336,
    'h': 280,
    'f': "large rectangle"
}, {
    'w': 468,
    'h': 60,
    'f': "banner"
}, {
    'w': 728,
    'h': 90,
    'f': "leaderboard"
},{
    'w': 300,
    'h': 1050,
    'f': "portrait"
}, {
    'w': 970,
    'h': 250,
    'f': "billboard"
}, {
    'w': 750,
    'h': 200,
    'f': "double billboard (reg.)"
}, {
    'w': 580,
    'h': 400,
    'f': "netboard (reg.)"
}]

ad = []

for x in Z:
  ad.append([x['w'] * x['h'], x['w'] , x['h'], x['f'] ])

ad.sort()

for a in ad:
  print "%4i px * %4i px = %6s px2  [%25s]" % (a[1], a[2], a[0], a[3])

