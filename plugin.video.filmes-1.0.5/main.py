# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {
 'filmes': [
 {
    'name': '007_contra_spectre',
    'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/007_contra_spectre.jpg',
    'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/007_contra_spectre.jpg',
    'video': 'http://192.168.0.10:8080/midias/Filmes/007_Contra_Spectre.mp4',
    'genre': ''}, 
	{
	  'name': 'Os Tres Mosqueteiros',
    'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/Os_Três_Mosqueteiros_fan.jpg',
    'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/Os_Três_Mosqueteiros.jpg',
    'video': 'http://192.168.0.10:8080/midias/Filmes/Os_Três_Mosqueteiros.mkv',
    'genre': ''},

    {'name': 'aladdin',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/aladdin.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/aladdin.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Aladdin.mkv',
     'genre': ''},

    {'name': 'asterix_1_o_gaulês_(1967)_720p_dual_johnl',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/asterix_1_o_gaulês_(1967)_720p_dual_johnl.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/asterix_1_o_gaulês_(1967)_720p_dual_johnl.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Asterix_1_O_Gaulês_(1967)_720p_Dual_JohnL.mkv',
     'genre': ''},

    {'name': 'conan,_o_bárbaro_(1982)_brrip_blu-ray_720p_dublado_dat2014',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/conan,_o_bárbaro_(1982)_brrip_blu-ray_720p_dublado_dat2014.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/conan,_o_bárbaro_(1982)_brrip_blu-ray_720p_dublado_dat2014.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Conan,_o_Bárbaro_(1982)_BRrip_Blu-Ray_720p_Dublado_Dat2014.mp4',
     'genre': ''},

    {'name': 'conan.o.destruidor',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/conan.o.destruidor.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/conan.o.destruidor.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Conan.O.Destruidor.mkv',
     'genre': ''},

    {'name': 'de_volta_ao_jogo_',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/de_volta_ao_jogo_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/de_volta_ao_jogo_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/De_Volta_ao_Jogo_.mp4',
     'genre': ''},

    {'name': 'duro_de_matar_1_-_dual_Áudio',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/duro_de_matar_1_-_dual_Áudio.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/duro_de_matar_1_-_dual_Áudio.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Duro_de_Matar_1_-_Dual_Áudio.mp4',
     'genre': ''},

    {'name': 'duro_de_matar_2_-_dual_Áudio',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/duro_de_matar_2_-_dual_Áudio.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/duro_de_matar_2_-_dual_Áudio.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Duro_de_Matar_2_-_Dual_Áudio.mp4',
     'genre': ''},

    {'name': 'duro_de_matar_3_-_dual_Áudio',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/duro_de_matar_3_-_dual_Áudio.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/duro_de_matar_3_-_dual_Áudio.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Duro_de_Matar_3_-_Dual_Áudio.mp4',
     'genre': ''},

    {'name': 'duro_de_matar_4_',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/duro_de_matar_4_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/duro_de_matar_4_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Duro_de_Matar_4_.mp4',
     'genre': ''},

    {'name': 'duro_de_matar_5_-_dual_Áudio',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/duro_de_matar_5_-_dual_Áudio.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/duro_de_matar_5_-_dual_Áudio.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Duro_de_Matar_5_-_Dual_Áudio.mp4',
     'genre': ''},

    {'name': 'feitiço_de_aquila.1985.720p.dublado.mv73',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/feitiço_de_aquila.1985.720p.dublado.mv73.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/feitiço_de_aquila.1985.720p.dublado.mv73.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Feitiço_de_Aquila.1985.720p.Dublado.MV73.mkv',
     'genre': ''},

    {'name': 'footloose_ritmo_contagiante',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/footloose_ritmo_contagiante.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/footloose_ritmo_contagiante.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Footloose_Ritmo_Contagiante.mkv',
     'genre': ''},

    {'name': 'footloose_–_ritmo_louco_(1984)_bdrip_720p_dual_Áudio_dat2014',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/footloose_–_ritmo_louco_(1984)_bdrip_720p_dual_Áudio_dat2014.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/footloose_–_ritmo_louco_(1984)_bdrip_720p_dual_Áudio_dat2014.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Footloose_–_Ritmo_Louco_(1984)_BDrip_720p_Dual_Áudio_dat2014.mkv',
     'genre': ''},

    {'name': 'fuga_de_nova_york_[1982]_-_bluray_720p_dublado',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/fuga_de_nova_york_[1982]_-_bluray_720p_dublado.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/fuga_de_nova_york_[1982]_-_bluray_720p_dublado.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Fuga_de_Nova_York_[1982]_-_BluRay_720p_Dublado.mkv',
     'genre': ''},

    {'name': 'fúria_de_titas_',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/fúria_de_titas_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/fúria_de_titas_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Fúria_de_Titas_.mp4',
     'genre': ''},

    {'name': 'highlander.(1986)',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/highlander.(1986).jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/highlander.(1986).jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Highlander.(1986).mkv',
     'genre': ''},

    {'name': 'independence_day_',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/independence_day_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/independence_day_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Independence_Day_.mp4',
     'genre': ''},

    {'name': 'john_wick_-_um_novo_dia_para_matar_2017',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/john_wick_-_um_novo_dia_para_matar_2017.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/john_wick_-_um_novo_dia_para_matar_2017.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/John_Wick_-_Um_Novo_Dia_Para_Matar_2017.mp4',
     'genre': ''},

    {'name': 'john_wick_chapter_3_-_parabellum',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/john_wick_chapter_3_-_parabellum.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/john_wick_chapter_3_-_parabellum.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/John_Wick_Chapter_3_-_Parabellum.mkv',
     'genre': ''},

    {'name': 'krull',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/krull.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/krull.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Krull.mp4',
     'genre': ''},

    {'name': 'nascido_para_matar_1080p_(1987)_dublado_-_ytsbr.com',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/nascido_para_matar_1080p_(1987)_dublado_-_ytsbr.com.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/nascido_para_matar_1080p_(1987)_dublado_-_ytsbr.com.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Nascido_Para_Matar_1080p_(1987)_Dublado_-_YTSBR.COM.mp4',
     'genre': ''},

    {'name': 'o_jogo_da_imitacao',
      'fanart':'http://192.168.0.10:8080/midias/Filmes/img/o_jogo_da_imitacao.jpg',
      'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/o_jogo_da_imitacao.jpg',
      'video': 'http://192.168.0.10:8080/midias/Filmes/O_jogo_da_imitacao.mkv',
      'genre': ''},

    {'name': 'o.rei.leao.2019.720p.bluray.x264-dual.comandotorrents.com',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/o.rei.leao.2019.720p.bluray.x264-dual.comandotorrents.com.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/o.rei.leao.2019.720p.bluray.x264-dual.comandotorrents.com.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/O.Rei.Leao.2019.720p.BluRay.x264-DUAL.COMANDOTORRENTS.COM.mkv',
     'genre': ''},

    {'name': 'osmose.jones',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/osmose.jones.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/osmose.jones.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Osmose.Jones.mkv',
     'genre': ''},

    {'name': 'o_auto_da_compadecida_(2000)_(2)',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/o_auto_da_compadecida_(2000)_(2).jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/o_auto_da_compadecida_(2000)_(2).jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/o_auto_da_compadecida_(2000)_(2).mp4',
     'genre': ''},

    {'name': 'o_exterminador_do_futuro_2_-_o_julgamento_final_(1991)_bluray_720p_dublado',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/o_exterminador_do_futuro_2_-_o_julgamento_final_(1991)_bluray_720p_dublado.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/o_exterminador_do_futuro_2_-_o_julgamento_final_(1991)_bluray_720p_dublado.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/O_Exterminador_Do_Futuro_2_-_O_Julgamento_Final_(1991)_BluRay_720p_Dublado.mkv',
     'genre': ''},

    {'name': 'o_grande_dragão_branco',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/o_grande_dragão_branco.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/o_grande_dragão_branco.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/O_Grande_Dragão_Branco.MP4',
     'genre': ''},

    {'name': 'o_predador__(1987)_bdrip_720p_dublado_dat2014',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/o_predador__(1987)_bdrip_720p_dublado_dat2014.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/o_predador__(1987)_bdrip_720p_dublado_dat2014.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/O_Predador__(1987)_BDrip_720p_Dublado_dat2014.mp4',
     'genre': ''},

    {'name': 'o_ultimo_dos_moicanos_dublado',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/o_ultimo_dos_moicanos_dublado.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/o_ultimo_dos_moicanos_dublado.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/O_Ultimo_dos_Moicanos_Dublado.avi',
     'genre': ''},

    {'name': 'pink_floyd_the_wall_(1982)[dvdrip][big_dad_e™]',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/pink_floyd_the_wall_(1982)[dvdrip][big_dad_e™].jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/pink_floyd_the_wall_(1982)[dvdrip][big_dad_e™].jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Pink_Floyd_The_Wall_(1982)[DVDRip][big_dad_e™].avi',
     'genre': ''},

    {'name': 'pokémon.o.filme.mewtwo.contra.ataca.1080p.bluray.h264.ac3.2.0-5.1.dual-mld',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/pokémon.o.filme.mewtwo.contra.ataca.1080p.bluray.h264.ac3.2.0-5.1.dual-mld.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/pokémon.o.filme.mewtwo.contra.ataca.1080p.bluray.h264.ac3.2.0-5.1.dual-mld.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Pokémon.O.Filme.Mewtwo.Contra.Ataca.1080p.BluRay.H264.AC3.2.0-5.1.DUAL-MLD.mkv',
     'genre': ''},

    {'name': 'primal.fear.1996.720p.bluray.x264.yify',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/primal.fear.1996.720p.bluray.x264.yify.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/primal.fear.1996.720p.bluray.x264.yify.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Primal.Fear.1996.720p.BluRay.x264.YIFY.mkv',
     'genre': ''},

    {'name': 'projeto_gemini_2019',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/projeto_gemini_2019.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/projeto_gemini_2019.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Projeto_Gemini_2019.mkv',
     'genre': ''},

    {'name': 'rambo_ii_-_a_missão_(1985)720p.bluray.5.1.x264.dual-www.bludv.com',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/rambo_ii_-_a_missão_(1985)720p.bluray.5.1.x264.dual-www.bludv.com.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/rambo_ii_-_a_missão_(1985)720p.bluray.5.1.x264.dual-www.bludv.com.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Rambo_II_-_A_Missão_(1985)720p.BluRay.5.1.x264.DUAL-WWW.BLUDV.COM.mkv',
     'genre': ''},

    {'name': 'robin.hood_-_a_origem_2019',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/robin.hood_-_a_origem_2019.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/robin.hood_-_a_origem_2019.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Robin.Hood_-_A_Origem_2019.mp4',
     'genre': ''},

    {'name': 'robin_hood_-_o_príncipe_dos_ladrões_(1991)_brrip_blu-ray_720p_dublado_dat2015',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/robin_hood_-_o_príncipe_dos_ladrões_(1991)_brrip_blu-ray_720p_dublado_dat2015.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/robin_hood_-_o_príncipe_dos_ladrões_(1991)_brrip_blu-ray_720p_dublado_dat2015.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Robin_Hood_-_O_Príncipe_dos_Ladrões_(1991)_BRrip_Blu-Ray_720p_Dublado_Dat2015.mp4',
     'genre': ''},

    {'name': 'sniper.americano.2015.1080p.dual-wolverdonfilmes.com',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/sniper.americano.2015.1080p.dual-wolverdonfilmes.com.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/sniper.americano.2015.1080p.dual-wolverdonfilmes.com.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Sniper.Americano.2015.1080p.Dual-WOLVERDONFILMES.COM.mkv',
     'genre': ''},

    {'name': 'ta_chovendo_hamburguer_1_(2009)_1080p_dual_johnl',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/ta_chovendo_hamburguer_1_(2009)_1080p_dual_johnl.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/ta_chovendo_hamburguer_1_(2009)_1080p_dual_johnl.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Ta_Chovendo_Hamburguer_1_(2009)_1080p_Dual_JohnL.mkv',
     'genre': ''},

    {'name': 'toy.story.4.2019.720p.bluray.x264.dual-comandotorrents.com',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/toy.story.4.2019.720p.bluray.x264.dual-comandotorrents.com.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/toy.story.4.2019.720p.bluray.x264.dual-comandotorrents.com.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Toy.Story.4.2019.720p.BluRay.x264.DUAL-COMANDOTORRENTS.COM.mkv',
     'genre': ''},

    {'name': 'um_dia_de_fúria_(1993)_bdrip_720p_dublado_dat2014',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/um_dia_de_fúria_(1993)_bdrip_720p_dublado_dat2014.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/um_dia_de_fúria_(1993)_bdrip_720p_dublado_dat2014.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Um_Dia_de_Fúria_(1993)_BDrip_720p_Dublado_dat2014.mp4',
     'genre': ''},

    {'name': 'venom.2018.720p.bluray.x264.dublado-www.bludv.tv',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/venom.2018.720p.bluray.x264.dublado-www.bludv.tv.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/venom.2018.720p.bluray.x264.dublado-www.bludv.tv.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Venom.2018.720p.BluRay.x264.DUBLADO-WWW.BLUDV.TV.mp4',
     'genre': ''},

    {'name': 'vingadores.ultimato.2019.720p.bluray.x264-dublado-www.comandotorrents.com',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/vingadores.ultimato.2019.720p.bluray.x264-dublado-www.comandotorrents.com.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/vingadores.ultimato.2019.720p.bluray.x264-dublado-www.comandotorrents.com.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Vingadores.Ultimato.2019.720p.BluRay.x264-DUBLADO-WWW.COMANDOTORRENTS.COM.mp4',
     'genre': ''},

    {'name': 'warriors_-_os_selvagens_da_noite_[1979]_-_bluray_720p_dublado',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/warriors_-_os_selvagens_da_noite_[1979]_-_bluray_720p_dublado.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/warriors_-_os_selvagens_da_noite_[1979]_-_bluray_720p_dublado.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/Warriors_-_Os_Selvagens_da_Noite_[1979]_-_BluRay_720p_Dublado.mkv',
     'genre': ''},

    {'name': 'wifi_ralph_quebrando.a.internet.2019.720p',
     'fanart': 'http://192.168.0.10:8080/midias/Filmes/img/wifi_ralph_quebrando.a.internet.2019.720p.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Filmes/img/wifi_ralph_quebrando.a.internet.2019.720p.jpg',
     'video': 'http://192.168.0.10:8080/midias/Filmes/WiFi_Ralph_Quebrando.a.Internet.2019.720p.mp4',
     'genre': ''},

],


   'As Aventurar de TinTin' : [

        {'name': 'as_aventuras_de_tintin_s01ep01',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep01.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep01.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP01.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep02',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep02.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep02.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP02.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep03',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep03.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep03.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP03.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep04',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep04.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep04.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP04.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep05',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep05.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep05.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP05.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep06',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep06.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep06.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP06.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep07',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep07.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep07.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP07.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep08',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep08.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep08.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP08.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep09',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep09.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep09.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP09.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep10',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep10.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep10.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP10.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep11',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep11.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep11.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP11.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep12',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep12.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep12.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP12.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep13',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep13.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep13.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP13.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep14',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep14.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep14.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP14.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep15',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep15.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep15.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP15.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep16',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep16.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep16.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP16.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep17',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep17.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep17.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP17.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep18',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep18.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep18.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP18.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep19',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep19.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep19.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP19.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep20',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep20.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep20.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP20.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep21',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep21.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep21.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP21.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep22',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep22.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep22.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP22.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep23',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep23.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep23.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP23.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep24',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep24.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep24.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP24.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep25',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep25.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep25.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP25.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep26',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep26.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep26.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP26.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep27',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep27.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep27.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP27.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep28',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep28.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep28.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP28.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep29',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep29.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep29.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP29.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep30',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep30.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep30.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP30.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep31',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep31.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep31.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP31.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep32',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep32.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep32.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP32.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep33',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep33.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep33.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP33.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep34',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep34.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep34.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP34.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep35',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep35.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep35.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP35.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep36',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep36.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep36.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP36.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep37',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep37.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep37.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP37.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep38',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep38.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep38.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP38.mp4',
         'genre': ''},

        {'name': 'as_aventuras_de_tintin_s01ep39',
         'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep39.jpg',
         'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/as_aventuras_de_tintin_s01ep39.jpg',
         'video': 'http://192.168.0.10:8080/midias/Desenhos/As_Aventuras_de_TinTin_S01EP39.mp4',
         'genre': ''},
    ],
	
		
				'Os padrinhos Mágicos':[
				{'name': 'padrinhos_magicos-s01e01.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e01.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e01.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_magicos-S01E01.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s01e02.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e02.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e02.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_magicos-S01E02.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s01e03.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e03.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e03.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_magicos-S01E03.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s01e04.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e04.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e04.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_magicos-S01E04.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s01e05.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e05.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e05.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_magicos-S01E05.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s01e06.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e06.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e06.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_magicos-S01E06.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s01e07.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e07.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e07.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_magicos-S01E07.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s01e08.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e08.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e08.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_magicos-S01E08.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s01e09.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e09.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e09.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_magicos-S01E09.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s01e10.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e10.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e10.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_magicos-S01E10.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s01e11.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e11.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e11.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_magicos-S01E11.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s01e12.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e12.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s01e12.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_magicos-S01E12.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e01.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e01.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e01.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E01.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e02.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e02.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e02.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E02.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e03.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e03.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e03.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E03.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e04.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e04.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e04.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E04.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e05.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e05.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e05.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E05.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e06.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e06.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e06.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E06.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e07.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e07.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e07.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E07.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e08.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e08.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e08.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E08.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e09.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e09.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e09.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E09.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e10.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e10.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e10.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E10.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e11.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e11.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e11.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E11.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e12.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e12.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e12.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E12.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e13.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e13.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e13.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E13.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e14.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e14.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e14.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E14.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e15.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e15.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e15.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E15.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e16.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e16.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e16.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E16.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e17.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e17.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e17.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E17.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e18.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e18.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e18.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E18.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e19.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e19.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e19.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E19.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e20.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e20.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e20.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E20.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e21.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e21.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e21.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E21.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e22.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e22.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e22.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E22.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e23.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e23.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e23.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E23.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e24.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e24.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e24.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E24.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e25.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e25.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e25.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E25.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e26.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e26.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e26.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E26.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e27.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e27.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e27.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E27.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e28.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e28.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e28.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E28.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e29.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e29.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e29.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E29.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e30.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e30.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e30.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E30.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e31.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e31.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e31.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E31.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e32.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e32.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e32.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E32.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e33.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e33.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e33.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E33.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e34.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e34.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e34.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E34.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e35.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e35.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e35.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E35.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s02e36.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e36.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s02e36.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S02E36.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e01.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e01.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e01.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E01.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e02.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e02.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e02.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E02.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e03.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e03.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e03.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E03.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e04.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e04.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e04.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E04.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e05.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e05.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e05.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E05.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e06.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e06.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e06.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E06.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e07.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e07.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e07.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E07.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e08.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e08.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e08.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E08.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e09.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e09.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e09.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E09.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e10.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e10.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e10.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E10.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e11.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e11.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e11.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E11.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e12.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e12.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e12.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E12.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e13.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e13.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e13.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E13.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e14.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e14.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e14.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E14.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e15.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e15.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e15.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E15.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e16.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e16.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e16.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E16.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e17.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e17.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e17.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E17.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e18.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e18.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e18.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E18.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e19.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e19.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e19.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E19.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e20.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e20.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e20.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E20.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e21.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e21.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e21.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E21.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e22.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e22.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e22.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E22.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s03e23.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e23.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s03e23.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S03E23.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e01.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e01.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e01.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E01.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e02.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e02.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e02.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E02.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e03.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e03.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e03.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E03.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e04.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e04.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e04.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E04.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e05.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e05.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e05.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E05.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e06.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e06.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e06.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E06.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e07.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e07.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e07.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E07.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e08.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e08.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e08.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E08.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e09.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e09.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e09.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E09.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e10.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e10.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e10.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E10.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e11.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e11.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e11.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E11.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e12.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e12.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e12.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E12.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e13.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e13.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e13.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E13.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e14.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e14.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e14.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E14.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e15.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e15.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e15.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E15.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e16.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e16.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e16.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E16.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e17.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e17.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e17.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E17.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e18.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e18.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e18.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E18.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e19.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e19.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e19.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E19.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e20.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e20.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e20.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E20.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e21.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e21.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e21.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E21.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s04e22.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e22.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s04e22.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S04E22.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e01.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e01.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e01.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E01.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e02.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e02.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e02.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E02.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e03.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e03.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e03.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E03.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e04.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e04.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e04.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E04.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e05.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e05.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e05.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E05.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e06.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e06.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e06.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E06.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e07.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e07.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e07.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E07.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e08.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e08.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e08.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E08.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e09.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e09.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e09.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E09.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e10.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e10.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e10.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E10.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e11.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e11.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e11.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E11.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e12.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e12.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e12.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E12.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e13.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e13.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e13.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E13.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e14.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e14.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e14.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E14.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e15.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e15.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e15.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E15.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e16.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e16.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e16.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E16.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e17.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e17.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e17.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E17.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e18.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e18.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e18.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E18.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e19.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e19.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e19.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E19.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e20.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e20.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e20.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E20.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e21.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e21.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e21.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E21.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e22.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e22.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e22.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E22.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e23.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e23.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e23.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E23.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e24.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e24.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e24.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E24.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e25.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e25.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e25.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E25.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e26.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e26.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e26.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E26.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s05e27.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e27.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s05e27.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S05E27.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s06e01.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e01.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e01.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S06E01.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s06e02.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e02.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e02.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S06E02.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s06e03.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e03.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e03.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S06E03.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s06e04.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e04.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e04.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S06E04.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s06e05.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e05.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e05.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S06E05.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s06e06.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e06.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e06.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S06E06.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s06e07.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e07.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e07.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S06E07.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s06e08.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e08.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e08.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S06E08.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s06e09.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e09.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e09.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S06E09.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s06e10.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e10.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e10.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S06E10.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s06e11.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e11.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e11.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S06E11.rmvb.avi',
			'genre': ''},

			{'name': 'padrinhos_magicos-s06e12.rmvb',
			'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e12.rmvb.jpg',
			'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/padrinhos_magicos-s06e12.rmvb.jpg',
			'video': 'http://192.168.0.10:8080/midias/Desenhos/Padrinhos_Magicos-S06E12.rmvb.avi',
			'genre': ''},
		
		],
		


  'Bob Esponja': [

    {'name': 'bob_esponja_s03e01',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e01.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e01.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E01.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e02',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e02.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e02.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E02.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e03',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e03.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e03.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E03.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e04',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e04.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e04.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E04.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e05',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e05.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e05.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E05.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e06',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e06.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e06.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E06.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e07',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e07.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e07.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E07.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e08',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e08.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e08.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E08.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e09',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e09.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e09.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E09.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e10',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e10.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e10.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E10.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e11',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e11.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e11.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E11.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e12',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e12.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e12.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E12.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e13',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e13.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e13.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E13.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e14',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e14.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e14.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E14.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e15',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e15.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e15.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E15.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e16',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e16.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e16.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E16.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e17',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e17.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e17.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E17.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e18',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e18.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e18.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E18.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e19',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e19.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e19.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E19.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e20',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e20.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e20.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E20.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e21',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e21.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e21.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E21.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e22',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e22.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e22.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E22.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e23',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e23.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e23.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E23.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e24',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e24.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e24.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E24.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e25',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e25.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e25.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E25.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e26',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e26.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e26.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E26.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e27',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e27.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e27.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E27.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e28',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e28.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e28.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E28.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e29',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e29.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e29.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E29.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e30',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e30.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e30.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E30.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e31',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e31.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e31.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E31.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e32',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e32.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e32.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E32.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e33',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e33.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e33.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E33.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e34',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e34.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e34.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E34.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e35',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e35.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e35.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E35.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e36',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e36.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e36.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E36.avi',
     'genre': ''},

    {'name': 'bob_esponja_s03e37',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e37.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s03e37.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S03E37.avi',
     'genre': ''},

    {'name': 'bob_esponja_s04e01',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e01.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e01.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E01.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e02',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e02.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e02.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E02.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e03',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e03.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e03.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E03.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e04',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e04.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e04.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E04.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e05',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e05.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e05.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E05.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e06',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e06.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e06.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E06.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e07',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e07.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e07.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E07.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e08',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e08.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e08.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E08.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e09',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e09.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e09.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E09.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e10',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e10.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e10.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E10.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e11',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e11.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e11.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E11.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e12',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e12.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e12.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E12.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e13',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e13.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e13.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E13.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e14',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e14.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e14.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E14.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e15',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e15.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e15.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E15.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e16',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e16.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e16.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E16.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e17',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e17.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e17.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E17.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e18',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e18.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e18.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E18.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e19',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e19.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e19.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E19.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e20',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e20.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e20.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E20.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e21',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e21.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e21.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E21.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e22',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e22.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e22.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E22.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e23',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e23.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e23.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E23.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e24',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e24.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e24.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E24.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e25',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e25.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e25.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E25.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e26',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e26.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e26.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E26.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e27',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e27.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e27.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E27.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e28',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e28.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e28.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E28.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e29',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e29.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e29.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E29.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e30',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e30.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e30.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E30.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e31',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e31.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e31.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E31.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e32',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e32.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e32.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E32.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e33',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e33.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e33.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E33.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e34',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e34.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e34.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E34.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e35',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e35.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e35.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E35.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e36',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e36.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e36.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E36.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e37',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e37.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e37.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E37.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s04e38',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e38.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s04e38.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S04E38.mp4',
     'genre': ''},

    {'name': 'bob_esponja_s05e01',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e01.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e01.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E01.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e02',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e02.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e02.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E02.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e03',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e03.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e03.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E03.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e04',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e04.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e04.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E04.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e05',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e05.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e05.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E05.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e06',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e06.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e06.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E06.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e07',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e07.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e07.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E07.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e08',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e08.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e08.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E08.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e09',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e09.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e09.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E09.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e10',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e10.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e10.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E10.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e11',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e11.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e11.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E11.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e12',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e12.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e12.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E12.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e13',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e13.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e13.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E13.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e14',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e14.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e14.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E14.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e15',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e15.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e15.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E15.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e16',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e16.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e16.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E16.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e17',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e17.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e17.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E17.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e18',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e18.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e18.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E18.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e19',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e19.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e19.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E19.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e20',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e20.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e20.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E20.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e21',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e21.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e21.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E21.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e22',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e22.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e22.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E22.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e23',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e23.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e23.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E23.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e24',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e24.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e24.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E24.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e25',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e25.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e25.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E25.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e26',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e26.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e26.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E26.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e27',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e27.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e27.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E27.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e28',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e28.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e28.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E28.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e29',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e29.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e29.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E29.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e30',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e30.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e30.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E30.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e31',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e31.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e31.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E31.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e32',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e32.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e32.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E32.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e33',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e33.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e33.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E33.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e34',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e34.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e34.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E34.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e35',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e35.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e35.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E35.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e36-37',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e36-37.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e36-37.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E36-37.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e38',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e38.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e38.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E38.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e39',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e39.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e39.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E39.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e40',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e40.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e40.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E40.avi',
     'genre': ''},

    {'name': 'bob_esponja_s05e41',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e41.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s05e41.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/BOB_ESPONJA_S05E41.avi',
     'genre': ''},
	 
	 {'name': 'bob_esponja_s6e01_-_casa_chique',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e01_-_casa_chique.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e01_-_casa_chique.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E01_-_Casa_chique.avi',
'genre': ''},

{'name': 'bob_esponja_s6e02_-_estrada_do_carsiri',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e02_-_estrada_do_carsiri.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e02_-_estrada_do_carsiri.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E02_-_Estrada_do_carsiri.avi',
'genre': ''},

{'name': 'bob_esponja_s6e03_-_doido_por_tostões',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e03_-_doido_por_tostões.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e03_-_doido_por_tostões.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E03_-_Doido_por_tostões.avi',
'genre': ''},

{'name': 'bob_esponja_s6e04_-_novato_náutico',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e04_-_novato_náutico.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e04_-_novato_náutico.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E04_-_Novato_náutico.avi',
'genre': ''},

{'name': 'bob_esponja_s6e05_-_songicus',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e05_-_songicus.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e05_-_songicus.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E05_-_Songicus.avi',
'genre': ''},

{'name': 'bob_esponja_s6e06_-_sinfonia_das_ventosas',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e06_-_sinfonia_das_ventosas.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e06_-_sinfonia_das_ventosas.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E06_-_Sinfonia_das_ventosas.avi',
'genre': ''},

{'name': 'bob_esponja_s6e07_-_não_é_normal',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e07_-_não_é_normal.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e07_-_não_é_normal.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E07_-_Não_é_normal.avi',
'genre': ''},

{'name': 'bob_esponja_s6e08_-_desaparecidos',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e08_-_desaparecidos.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e08_-_desaparecidos.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E08_-_Desaparecidos.avi',
'genre': ''},

{'name': 'bob_esponja_s6e09_-_a_farpa',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e09_-_a_farpa.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e09_-_a_farpa.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E09_-_A_farpa.avi',
'genre': ''},

{'name': 'bob_esponja_s6e10_-_os_palhaços_do_assobio',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e10_-_os_palhaços_do_assobio.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e10_-_os_palhaços_do_assobio.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E10_-_Os_palhaços_do_assobio.avi',
'genre': ''},

{'name': 'bob_esponja_s6e11_-_uma_vida_num_dia',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e11_-_uma_vida_num_dia.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e11_-_uma_vida_num_dia.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E11_-_Uma_vida_num_dia.avi',
'genre': ''},

{'name': 'bob_esponja_s6e12_-_alvejado',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e12_-_alvejado.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e12_-_alvejado.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E12_-_Alvejado.avi',
'genre': ''},

{'name': 'bob_esponja_s6e13_-_lula_molusco_gigante',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e13_-_lula_molusco_gigante.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e13_-_lula_molusco_gigante.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E13_-_Lula_molusco_gigante.avi',
'genre': ''},

{'name': 'bob_esponja_s6e14_-_nenhum_nariz_sabe',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e14_-_nenhum_nariz_sabe.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e14_-_nenhum_nariz_sabe.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E14_-_Nenhum_nariz_sabe.avi',
'genre': ''},

{'name': 'bob_esponja_s6e15_-_hamburguer_e_delito',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e15_-_hamburguer_e_delito.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e15_-_hamburguer_e_delito.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E15_-_Hamburguer_e_Delito.avi',
'genre': ''},

{'name': 'bob_esponja_s6e16_-_o_cliente_assíduo_do_plâncton',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e16_-_o_cliente_assíduo_do_plâncton.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e16_-_o_cliente_assíduo_do_plâncton.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E16_-_O_Cliente_assíduo_do_Plâncton.avi',
'genre': ''},

{'name': 'bob_esponja_s6e17_-_queridos_vikings',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e17_-_queridos_vikings.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e17_-_queridos_vikings.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E17_-_Queridos_Vikings.avi',
'genre': ''},

{'name': 'bob_esponja_s6e18_-_a_trapaça',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e18_-_a_trapaça.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e18_-_a_trapaça.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E18_-_A_trapaça.avi',
'genre': ''},

{'name': 'bob_esponja_s6e19_-_o_vovô_pirata',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e19_-_o_vovô_pirata.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e19_-_o_vovô_pirata.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E19_-_O_vovô_pirata.avi',
'genre': ''},

{'name': 'bob_esponja_s6e20_-_loja_maçonica_cefalopode',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e20_-_loja_maçonica_cefalopode.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e20_-_loja_maçonica_cefalopode.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E20_-_Loja_maçonica_cefalopode.avi',
'genre': ''},

{'name': 'bob_esponja_s6e21_-_embarque_atrapalhado',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e21_-_embarque_atrapalhado.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e21_-_embarque_atrapalhado.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E21_-_Embarque_atrapalhado.avi',
'genre': ''},

{'name': 'bob_esponja_s6e22_-_professor_lula_molusco',
'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e22_-_professor_lula_molusco.jpg',
'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/bob_esponja_s6e22_-_professor_lula_molusco.jpg',
'video': 'http://192.168.0.10:8080/midias/Desenhos/Bob_esponja_S6E22_-_Professor_Lula_Molusco.avi',
'genre': ''},
],

    'A Corrida Maluca': [

    {'name': 'corrida.maluca.05.g.p.missouri',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.05.g.p.missouri.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.05.g.p.missouri.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.05.G.P.Missouri.avi',
     'genre': ''},

    {'name': 'corrida.maluca.06.g.p.idaho',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.06.g.p.idaho.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.06.g.p.idaho.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.06.G.P.Idaho.avi',
     'genre': ''},

    {'name': 'corrida.maluca.07.a_etapa_de_baja',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.07.a_etapa_de_baja.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.07.a_etapa_de_baja.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.07.A_Etapa_de_Baja.avi',
     'genre': ''},

    {'name': 'corrida.maluca.08.um.gorila.na.corrida',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.08.um.gorila.na.corrida.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.08.um.gorila.na.corrida.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.08.Um.Gorila.na.Corrida.avi',
     'genre': ''},

    {'name': 'corrida.maluca.09.g.p.bem_no_coração',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.09.g.p.bem_no_coração.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.09.g.p.bem_no_coração.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.09.G.P.Bem_no_Coração.avi',
     'genre': ''},

    {'name': 'corrida.maluca.10.g.p.virginia',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.10.g.p.virginia.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.10.g.p.virginia.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.10.G.P.Virginia.avi',
     'genre': ''},

    {'name': 'corrida.maluca.11.g.p.altos.e.baixos',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.11.g.p.altos.e.baixos.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.11.g.p.altos.e.baixos.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.11.G.P.Altos.e.Baixos.avi',
     'genre': ''},

    {'name': 'corrida.maluca.12.a_toda_velocidade_para_arkansas',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.12.a_toda_velocidade_para_arkansas.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.12.a_toda_velocidade_para_arkansas.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.12.A_Toda_Velocidade_para_Arkansas.avi',
     'genre': ''},

    {'name': 'corrida.maluca.13.g.p.de_mississippi.ceniks',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.13.g.p.de_mississippi.ceniks.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.13.g.p.de_mississippi.ceniks.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/corrida.maluca.13.g.p.de_mississippi.ceniks.avi',
     'genre': ''},

    {'name': 'corrida.maluca.14.g.p.alabama.por.ceniks',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.14.g.p.alabama.por.ceniks.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.14.g.p.alabama.por.ceniks.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.14.G.P.Alabama.por.ceniks.avi',
     'genre': ''},

    {'name': 'corrida.maluca.15.corrida_quente_em_chillicothe',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.15.corrida_quente_em_chillicothe.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.15.corrida_quente_em_chillicothe.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.15.Corrida_Quente_em_Chillicothe.avi',
     'genre': ''},

    {'name': 'corrida.maluca.16.g.p.a_estrada_não_era_essa.por.ceniks',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.16.g.p.a_estrada_não_era_essa.por.ceniks.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.16.g.p.a_estrada_não_era_essa.por.ceniks.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.16.G.P.A_Estrada_Não_Era_Essa.por.ceniks.avi',
     'genre': ''},

    {'name': 'corrida.maluca.17.g.p.rhode_island.por.ceniks',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.17.g.p.rhode_island.por.ceniks.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.17.g.p.rhode_island.por.ceniks.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.17.G.P.Rhode_Island.por.ceniks.avi',
     'genre': ''},

    {'name': 'corrida.maluca.18.g.p.pólo_norte.por.ceniks',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.18.g.p.pólo_norte.por.ceniks.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.18.g.p.pólo_norte.por.ceniks.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.18.G.P.Pólo_Norte.por.ceniks.avi',
     'genre': ''},

    {'name': 'corrida.maluca.19.g.p.vale_tudo.por.ceniks',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.19.g.p.vale_tudo.por.ceniks.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.19.g.p.vale_tudo.por.ceniks.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.19.G.P.Vale_Tudo.por.ceniks.avi',
     'genre': ''},

    {'name': 'corrida.maluca.20.g.p.texas',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.20.g.p.texas.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.20.g.p.texas.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.20.G.P.Texas.avi',
     'genre': ''},

    {'name': 'corrida.maluca.21.g.p.washington',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.21.g.p.washington.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.21.g.p.washington.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.21.G.P.Washington.avi',
     'genre': ''},

    {'name': 'corrida.maluca.22.g.p.do.deserto.por.ceniks',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.22.g.p.do.deserto.por.ceniks.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.22.g.p.do.deserto.por.ceniks.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.22.G.P.do.Deserto.por.ceniks.avi',
     'genre': ''},

    {'name': 'corrida.maluca.23.g.p.uni.duni.te.por.ceniks',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.23.g.p.uni.duni.te.por.ceniks.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.23.g.p.uni.duni.te.por.ceniks.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.23.G.P.Uni.Duni.Te.por.ceniks.avi',
     'genre': ''},

    {'name': 'corrida.maluca.24.g.p.dos.pântanos.ceniks_(1)',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.24.g.p.dos.pântanos.ceniks_(1).jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.24.g.p.dos.pântanos.ceniks_(1).jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/corrida.maluca.24.g.p.dos.pântanos.ceniks_(1).avi',
     'genre': ''},

    {'name': 'corrida.maluca.25.g.p.dakota.por.ceniks.avi',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.25.g.p.dakota.por.ceniks.avi.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.25.g.p.dakota.por.ceniks.avi.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.25.G.P.Dakota.por.ceniks.avi.avi',
     'genre': ''},

    {'name': 'corrida.maluca.26.g.p.delaware.por.ceniks',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.26.g.p.delaware.por.ceniks.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.26.g.p.delaware.por.ceniks.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/corrida.maluca.26.g.p.delaware.por.ceniks.avi',
     'genre': ''},

    {'name': 'corrida.maluca.27.g.p.jollywood.ceniks',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.27.g.p.jollywood.ceniks.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.27.g.p.jollywood.ceniks.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.27.G.P.Jollywood.ceniks.avi',
     'genre': ''},

    {'name': 'corrida.maluca.28.g.p.raleigh',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.28.g.p.raleigh.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.28.g.p.raleigh.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.28.G.P.Raleigh.avi',
     'genre': ''},

    {'name': 'corrida.maluca.29.g.p.pennsylvania',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.29.g.p.pennsylvania.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.29.g.p.pennsylvania.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.29.G.P.Pennsylvania.avi',
     'genre': ''},

    {'name': 'corrida.maluca.30.g.p.h',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.30.g.p.h.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.30.g.p.h.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.30.G.P.H.avi',
     'genre': ''},

    {'name': 'corrida.maluca.31.g.p.idaho',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.31.g.p.idaho.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.31.g.p.idaho.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.31.G.P.Idaho.avi',
     'genre': ''},

    {'name': 'corrida.maluca.32.g.p.florida',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.32.g.p.florida.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.32.g.p.florida.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.32.G.P.Florida.avi',
     'genre': ''},

    {'name': 'corrida.maluca.33.g.p.racine',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.33.g.p.racine.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.33.g.p.racine.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.33.G.P.Racine.avi',
     'genre': ''},

    {'name': 'corrida.maluca.34.g.prêmio.carlsbad',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.34.g.prêmio.carlsbad.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/corrida.maluca.34.g.prêmio.carlsbad.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Corrida.Maluca.34.G.Prêmio.Carlsbad.avi',
     'genre': ''},

],



     'Pink e Celebro': [

    {'name': 'pinky_e_cerebro_-_s01e01',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e01.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e01.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E01.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e02',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e02.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e02.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E02.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e03',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e03.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e03.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E03.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e04',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e04.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e04.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E04.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e05',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e05.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e05.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E05.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e06',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e06.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e06.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E06.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e07',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e07.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e07.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E07.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e08',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e08.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e08.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E08.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e09',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e09.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e09.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E09.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e10',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e10.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e10.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E10.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e11',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e11.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e11.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E11.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e12',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e12.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e12.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E12.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e13',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e13.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e13.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E13.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e14',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e14.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e14.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E14.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e15',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e15.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e15.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E15.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e16',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e16.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e16.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E16.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e17',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e17.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e17.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E17.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e18',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e18.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e18.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E18.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e19',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e19.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e19.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E19.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e20',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e20.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e20.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E20.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e21',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e21.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e21.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E21.mp4',
     'genre': ''},

    {'name': 'pinky_e_cerebro_-_s01e22',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e22.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/pinky_e_cerebro_-_s01e22.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Pinky_e_Cerebro_-_S01E22.mp4',
     'genre': ''},
      ],

     'Space Goofs': [

    {'name': 'space_goofs_-_s01ep01_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep01_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep01_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP01_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep02_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep02_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep02_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP02_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep03_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep03_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep03_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP03_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep04_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep04_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep04_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP04_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep05_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep05_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep05_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP05_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep06_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep06_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep06_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP06_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep07_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep07_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep07_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP07_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep08_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep08_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep08_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP08_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep09_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep09_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep09_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP09_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep10_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep10_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep10_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP10_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep11_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep11_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep11_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP11_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep12_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep12_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep12_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP12_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep13_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep13_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep13_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP13_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep14_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep14_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep14_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP14_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep15_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep15_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep15_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP15_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep16_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep16_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep16_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP16_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep17_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep17_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep17_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP17_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep18_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep18_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep18_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP18_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep19_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep19_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep19_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP19_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep20_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep20_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep20_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP20_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep21_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep21_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep21_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP21_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep22_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep22_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep22_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP22_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep23_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep23_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep23_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP23_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep24_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep24_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep24_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP24_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep25_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep25_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep25_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP25_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep26_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep26_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep26_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP26_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep27_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep27_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep27_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP27_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep28_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep28_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep28_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP28_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep29_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep29_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep29_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP29_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep30_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep30_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep30_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP30_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep31_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep31_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep31_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP31_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep32_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep32_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep32_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP32_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep33_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep33_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep33_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP33_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep34_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep34_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep34_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP34_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep35_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep35_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep35_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP35_.avi',
     'genre': ''},

    {'name': 'space_goofs_-_s01ep36_',
     'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep36_.jpg',
     'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/space_goofs_-_s01ep36_.jpg',
     'video': 'http://192.168.0.10:8080/midias/Desenhos/Space_Goofs_-_S01EP36_.avi',
     'genre': ''},
     ],
    'Apenas um show':[

                         {'name': 'apenas_um_show_s01e01',
                          'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e01.jpg',
                          'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e01.jpg',
                          'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_s01e01.mkv',
                          'genre': ''},

                         {'name': 'apenas_um_show_s01e02',
                          'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e02.jpg',
                          'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e02.jpg',
                          'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_s01e02.mkv',
                          'genre': ''},

                         {'name': 'apenas_um_show_s01e03',
                          'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e03.jpg',
                          'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e03.jpg',
                          'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_s01e03.mkv',
                          'genre': ''},

                         {'name': 'apenas_um_show_s01e04',
                          'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e04.jpg',
                          'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e04.jpg',
                          'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_s01e04.mkv',
                          'genre': ''},

                         {'name': 'apenas_um_show_s01e05',
                          'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e05.jpg',
                          'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e05.jpg',
                          'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_s01e05.mkv',
                          'genre': ''},

                         {'name': 'apenas_um_show_s01e06',
                          'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e06.jpg',
                          'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e06.jpg',
                          'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_s01e06.mkv',
                          'genre': ''},

                         {'name': 'apenas_um_show_s01e07',
                          'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e07.jpg',
                          'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e07.jpg',
                          'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_s01e07.mkv',
                          'genre': ''},

                         {'name': 'apenas_um_show_s01e08',
                          'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e08.jpg',
                          'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e08.jpg',
                          'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_s01e08.mkv',
                          'genre': ''},

                         {'name': 'apenas_um_show_s01e09',
                          'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e09.jpg',
                          'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e09.jpg',
                          'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_s01e09.mkv',
                          'genre': ''},

                         {'name': 'apenas_um_show_s01e10',
                          'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e10.jpg',
                          'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e10.jpg',
                          'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_s01e10.mkv',
                          'genre': ''},

                         {'name': 'apenas_um_show_s01e11',
                          'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e11.jpg',
                          'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e11.jpg',
                          'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_s01e11.mkv',
                          'genre': ''},

                         {'name': 'apenas_um_show_s01e12',
                          'fanart': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e12.jpg',
                          'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s01e12.jpg',
                          'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_s01e12.mkv',
                          'genre': ''},

						{'name': 'apenas_um_show_s02e01',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e01.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e01.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E01.mp4',
						'genre': ''},

						{'name': 'apenas_um_show_s02e02 ',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e02 .jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e02 .jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E02 .wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e03',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e03.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e03.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E03.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e04',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e04.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e04.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E04.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e05',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e05.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e05.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E05.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e06',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e06.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e06.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E06.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e07',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e07.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e07.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E07.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e08',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e08.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e08.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E08.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e09',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e09.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e09.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E09.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e10',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e10.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e10.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E10.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e11',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e11.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e11.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E11.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e12',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e12.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e12.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E12.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e13',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e13.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e13.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E13.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e14',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e14.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e14.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E14.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e15',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e15.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e15.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E15.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e16',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e16.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e16.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E16.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e17',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e17.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e17.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E17.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e18',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e18.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e18.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E18.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e19',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e19.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e19.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E19.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e20',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e20.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e20.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E20.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e21',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e21.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e21.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E21.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e22',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e22.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e22.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E22.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e23',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e23.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e23.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E23.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e24',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e24.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e24.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E24.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e25',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e25.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e25.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E25.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e26',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e26.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e26.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E26.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e27',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e27.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e27.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E27.wmv',
						'genre': ''},

						{'name': 'apenas_um_show_s02e28',
						'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e28.jpg',
						'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/apenas_um_show_s02e28.jpg',
						'video': 'http://192.168.0.10:8080/midias/Desenhos/Apenas_um_show_S02E28.wmv',
						'genre': ''},

                     ],

                    'As meninas Super Poderosas':[

					{'name': 'amsp_s01e01',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e01.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e01.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E01.mkv',
					'genre': ''},

					{'name': 'amsp_s01e02',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e02.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e02.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E02.mkv',
					'genre': ''},

					{'name': 'amsp_s01e03',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e03.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e03.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E03.mkv',
					'genre': ''},

					{'name': 'amsp_s01e04',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e04.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e04.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E04.mkv',
					'genre': ''},

					{'name': 'amsp_s01e05',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e05.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e05.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E05.mkv',
					'genre': ''},

					{'name': 'amsp_s01e06',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e06.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e06.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E06.mkv',
					'genre': ''},

					{'name': 'amsp_s01e07',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e07.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e07.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E07.mkv',
					'genre': ''},

					{'name': 'amsp_s01e08',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e08.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e08.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E08.mkv',
					'genre': ''},

					{'name': 'amsp_s01e09',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e09.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e09.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E09.mkv',
					'genre': ''},

					{'name': 'amsp_s01e10',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e10.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e10.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E10.mkv',
					'genre': ''},

					{'name': 'amsp_s01e11',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e11.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e11.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E11.mkv',
					'genre': ''},

					{'name': 'amsp_s01e12',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e12.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e12.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E12.mkv',
					'genre': ''},

					{'name': 'amsp_s01e13',
					'fanart':'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e13.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Desenhos/img/amsp_s01e13.jpg',
					'video': 'http://192.168.0.10:8080/midias/Desenhos/AMSP_S01E13.mkv',
					'genre': ''},



                    ],

                     'documentarios': [
                      {'name': 'a_revoluÇÃo_dos_games__history',
                                        'fanart': 'http://192.168.0.10:8080/midias/Documentarios/img/a_revoluÇÃo_dos_games__history.jpg',
                                        'thumb': 'http://192.168.0.10:8080/midias/Documentarios/img/a_revoluÇÃo_dos_games__history.jpg',
                                        'video': 'http://192.168.0.10:8080/midias/Documentarios/A_REVOLUÇÃO_DOS_GAMES__HISTORY.mp4',
                                        'genre': ''},

                                       {
                                           'name': 'gigantes_dos_alimentos__episódio_1_empreendimentos_visionários__history',
                                           'fanart': 'http://192.168.0.10:8080/midias/Documentarios/img/gigantes_dos_alimentos__episódio_1_empreendimentos_visionários__history.jpg',
                                           'thumb': 'http://192.168.0.10:8080/midias/Documentarios/img/gigantes_dos_alimentos__episódio_1_empreendimentos_visionários__history.jpg',
                                           'video': 'http://192.168.0.10:8080/midias/Documentarios/GIGANTES_DOS_ALIMENTOS__Episódio_1_Empreendimentos_Visionários__HISTORY.mp4',
                                           'genre': ''},

                                       {'name': 'gigantes_dos_alimentos__episódio_2_ampliando_limites__history',
                                        'fanart': 'http://192.168.0.10:8080/midias/Documentarios/img/gigantes_dos_alimentos__episódio_2_ampliando_limites__history.jpg',
                                        'thumb': 'http://192.168.0.10:8080/midias/Documentarios/img/gigantes_dos_alimentos__episódio_2_ampliando_limites__history.jpg',
                                        'video': 'http://192.168.0.10:8080/midias/Documentarios/GIGANTES_DOS_ALIMENTOS__Episódio_2_Ampliando_Limites__HISTORY.mp4',
                                        'genre': ''},

                                       ],
									   'Todo Mundo Odeia o Cris': [{'name': '2x01_todo_mundo_odeia_rejeição',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x01_todo_mundo_odeia_rejeição.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x01_todo_mundo_odeia_rejeição.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x01_Todo_Mundo_Odeia_Rejeição.mp4',
					'genre': ''},

					{'name': '2x02_todo_mundo_odeia_o_presidente_do_grêmio',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x02_todo_mundo_odeia_o_presidente_do_grêmio.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x02_todo_mundo_odeia_o_presidente_do_grêmio.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x02_Todo_Mundo_Odeia_O_Presidente_do_Grêmio.mp4',
					'genre': ''},

					{'name': '2x03_todo_mundo_odeia_eleições',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x03_todo_mundo_odeia_eleições.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x03_todo_mundo_odeia_eleições.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x03_Todo_Mundo_Odeia_Eleições.mp4',
					'genre': ''},

					{'name': '2x04_todo_mundo_odeia_um_mentiroso',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x04_todo_mundo_odeia_um_mentiroso.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x04_todo_mundo_odeia_um_mentiroso.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x04_Todo_Mundo_Odeia_Um_Mentiroso.mp4',
					'genre': ''},

					{'name': '2x05_todo_mundo_odeia_malvo',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x05_todo_mundo_odeia_malvo.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x05_todo_mundo_odeia_malvo.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x05_Todo_Mundo_Odeia_Malvo.mp4',
					'genre': ''},

					{'name': '2x06_todo_mundo_odeia_sistema_de_parceiragem',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x06_todo_mundo_odeia_sistema_de_parceiragem.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x06_todo_mundo_odeia_sistema_de_parceiragem.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x06_Todo_Mundo_Odeia_Sistema_de_Parceiragem.mp4',
					'genre': ''},

					{'name': '2x07_todo_mundo_odeia_promessas',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x07_todo_mundo_odeia_promessas.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x07_todo_mundo_odeia_promessas.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x07_Todo_Mundo_Odeia_Promessas.mp4',
					'genre': ''},

					{'name': '2x08_todo_mundo_odeia_o_feriado',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x08_todo_mundo_odeia_o_feriado.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x08_todo_mundo_odeia_o_feriado.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x08_Todo_Mundo_Odeia_O_Feriado.mp4',
					'genre': ''},

					{'name': '2x09_todo_mundo_odeia_superstição',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x09_todo_mundo_odeia_superstição.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x09_todo_mundo_odeia_superstição.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x09_Todo_Mundo_Odeia_Superstição.mp4',
					'genre': ''},

					{'name': '2x10_todo_mundo_odeia_papai_noel',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x10_todo_mundo_odeia_papai_noel.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x10_todo_mundo_odeia_papai_noel.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x10_Todo_Mundo_Odeia_Papai_Noel.mp4',
					'genre': ''},

					{'name': '2x11_todo_mundo_odeia_ovos',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x11_todo_mundo_odeia_ovos.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x11_todo_mundo_odeia_ovos.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x11_Todo_Mundo_Odeia_Ovos.mp4',
					'genre': ''},

					{'name': '2x12_todo_mundo_odeia_os_inspetores',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x12_todo_mundo_odeia_os_inspetores.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x12_todo_mundo_odeia_os_inspetores.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x12_Todo_Mundo_Odeia_Os_Inspetores.mp4',
					'genre': ''},

					{'name': '2x13_todo_mundo_odeia_o_inverno',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x13_todo_mundo_odeia_o_inverno.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x13_todo_mundo_odeia_o_inverno.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x13_Todo_Mundo_Odeia_O_Inverno.mp4',
					'genre': ''},

					{'name': '2x14_todo_mundo_odeia_o_substituto',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x14_todo_mundo_odeia_o_substituto.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x14_todo_mundo_odeia_o_substituto.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x14_Todo_Mundo_Odeia_O_Substituto.mp4',
					'genre': ''},

					{'name': '2x15_todo_mundo_odeia_matar_aula',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x15_todo_mundo_odeia_matar_aula.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x15_todo_mundo_odeia_matar_aula.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x15_Todo_Mundo_Odeia_Matar_Aula.mp4',
					'genre': ''},

					{'name': '2x16_todo_mundo_odeia_roubar_correntes',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x16_todo_mundo_odeia_roubar_correntes.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x16_todo_mundo_odeia_roubar_correntes.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x16_Todo_Mundo_Odeia_Roubar_Correntes.mp4',
					'genre': ''},

					{'name': '2x17_todo_mundo_odeia_djs',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x17_todo_mundo_odeia_djs.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x17_todo_mundo_odeia_djs.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x17_Todo_Mundo_Odeia_DJs.mp4',
					'genre': ''},

					{'name': '2x18_todo_mundo_odeia_beisebol',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x18_todo_mundo_odeia_beisebol.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x18_todo_mundo_odeia_beisebol.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x18_Todo_Mundo_Odeia_Beisebol.mp4',
					'genre': ''},

					{'name': '2x19_todo_mundo_odeia_apostar',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x19_todo_mundo_odeia_apostar.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x19_todo_mundo_odeia_apostar.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x19_Todo_Mundo_Odeia_Apostar.mp4',
					'genre': ''},

					{'name': '2x20_todo_mundo_odeia_piadas_sujas',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x20_todo_mundo_odeia_piadas_sujas.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x20_todo_mundo_odeia_piadas_sujas.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x20_Todo_Mundo_Odeia_Piadas_Sujas.mp4',
					'genre': ''},

					{'name': '2x21_todo_mundo_odeia_matemática',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x21_todo_mundo_odeia_matemática.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x21_todo_mundo_odeia_matemática.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x21_Todo_Mundo_Odeia_Matemática.mp4',
					'genre': ''},

					{'name': '2x22_todo_mundo_odeia_o_Último_dia',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/2x22_todo_mundo_odeia_o_Último_dia.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/2x22_todo_mundo_odeia_o_Último_dia.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/2x22_Todo_Mundo_Odeia_O_Último_Dia.mp4',
					'genre': ''},

					{'name': '3x01_-_todo_mundo_odeia_o_orientador',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x01_-_todo_mundo_odeia_o_orientador.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x01_-_todo_mundo_odeia_o_orientador.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x01_-_Todo_Mundo_Odeia_O_Orientador.mp4',
					'genre': ''},

					{'name': '3x02_-_todo_mundo_odeia_o_caruso',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x02_-_todo_mundo_odeia_o_caruso.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x02_-_todo_mundo_odeia_o_caruso.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x02_-_Todo_Mundo_Odeia_O_Caruso.mp4',
					'genre': ''},

					{'name': '3x03_-todo_mundo_odeia_dirigir',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x03_-todo_mundo_odeia_dirigir.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x03_-todo_mundo_odeia_dirigir.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x03_-Todo_Mundo_Odeia_Dirigir.mp4',
					'genre': ''},

					{'name': '3x04_-_todo_mundo_odeia_o_cachorro',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x04_-_todo_mundo_odeia_o_cachorro.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x04_-_todo_mundo_odeia_o_cachorro.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x04_-_Todo_Mundo_Odeia_O_Cachorro.mp4',
					'genre': ''},

					{'name': '3x05_-_todo_mundo_odeia_casa_de_solteiro',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x05_-_todo_mundo_odeia_casa_de_solteiro.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x05_-_todo_mundo_odeia_casa_de_solteiro.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x05_-_Todo_Mundo_Odeia_Casa_de_Solteiro.mp4',
					'genre': ''},

					{'name': '3x06_todo_mundo_odeia_bed-stuy',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x06_todo_mundo_odeia_bed-stuy.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x06_todo_mundo_odeia_bed-stuy.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x06_Todo_Mundo_Odeia_Bed-Stuy.mp4',
					'genre': ''},

					{'name': '3x07_-_todo_mundo_odeia_hóspedes',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x07_-_todo_mundo_odeia_hóspedes.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x07_-_todo_mundo_odeia_hóspedes.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x07_-_Todo_Mundo_Odeia_Hóspedes.mp4',
					'genre': ''},

					{'name': '3x08_-_todo_mundo_odeia_salário_mínimo',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x08_-_todo_mundo_odeia_salário_mínimo.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x08_-_todo_mundo_odeia_salário_mínimo.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x08_-_Todo_Mundo_Odeia_Salário_Mínimo.mp4',
					'genre': ''},

					{'name': '3x09_-_todo_mundo_odeia_o_novato',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x09_-_todo_mundo_odeia_o_novato.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x09_-_todo_mundo_odeia_o_novato.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x09_-_Todo_Mundo_Odeia_O_Novato.mp4',
					'genre': ''},

					{'name': '3x10_-_todo_mundo_odeia_kwanzaa',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x10_-_todo_mundo_odeia_kwanzaa.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x10_-_todo_mundo_odeia_kwanzaa.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x10_-_Todo_Mundo_Odeia_Kwanzaa.mp4',
					'genre': ''},

					{'name': '3x11_-_todo_mundo_odeia_a_rodoviária',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x11_-_todo_mundo_odeia_a_rodoviária.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x11_-_todo_mundo_odeia_a_rodoviária.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x11_-_Todo_Mundo_Odeia_A_Rodoviária.mp4',
					'genre': ''},

					{'name': '3x12_-_todo_mundo_odeia_bad_boys',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x12_-_todo_mundo_odeia_bad_boys.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x12_-_todo_mundo_odeia_bad_boys.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x12_-_Todo_Mundo_Odeia_Bad_Boys.mp4',
					'genre': ''},

					{'name': '3x13_-_todo_mundo_odeia_o_primeiro_beijo',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x13_-_todo_mundo_odeia_o_primeiro_beijo.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x13_-_todo_mundo_odeia_o_primeiro_beijo.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x13_-_Todo_Mundo_Odeia_O_Primeiro_Beijo.mp4',
					'genre': ''},

					{'name': '3x14_-_todo_mundo_odeia_a_páscoa',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x14_-_todo_mundo_odeia_a_páscoa.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x14_-_todo_mundo_odeia_a_páscoa.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x14_-_Todo_Mundo_Odeia_A_Páscoa.mp4',
					'genre': ''},

					{'name': '3x15_-_todo_mundo_odeia_gretzky',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x15_-_todo_mundo_odeia_gretzky.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x15_-_todo_mundo_odeia_gretzky.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x15_-_Todo_Mundo_Odeia_Gretzky.mp4',
					'genre': ''},

					{'name': '3x16_-_todo_mundo_odeia_dfn',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x16_-_todo_mundo_odeia_dfn.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x16_-_todo_mundo_odeia_dfn.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x16_-_Todo_Mundo_Odeia_DFN.mp4',
					'genre': ''},

					{'name': '3x17_-_todo_mundo_odeia_ex-presidiários',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x17_-_todo_mundo_odeia_ex-presidiários.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x17_-_todo_mundo_odeia_ex-presidiários.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x17_-_Todo_Mundo_Odeia_Ex-Presidiários.mp4',
					'genre': ''},

					{'name': '3x18_-_todo_mundo_odeia_o_dia_da_terra',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x18_-_todo_mundo_odeia_o_dia_da_terra.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x18_-_todo_mundo_odeia_o_dia_da_terra.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x18_-_Todo_Mundo_Odeia_O_Dia_da_Terra.mp4',
					'genre': ''},

					{'name': '3x19_-_todo_mundo_odeia_ser_descolado',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x19_-_todo_mundo_odeia_ser_descolado.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x19_-_todo_mundo_odeia_ser_descolado.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x19_-_Todo_Mundo_Odeia_Ser_Descolado.mp4',
					'genre': ''},

					{'name': '3x20_-_todo_mundo_odeia_o_baile_da_nona_série',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x20_-_todo_mundo_odeia_o_baile_da_nona_série.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x20_-_todo_mundo_odeia_o_baile_da_nona_série.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x20_-_Todo_Mundo_Odeia_O_Baile_da_Nona_Série.mp4',
					'genre': ''},

					{'name': '3x21_-_todo_mundo_odeia_o_dia_das_mães',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x21_-_todo_mundo_odeia_o_dia_das_mães.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x21_-_todo_mundo_odeia_o_dia_das_mães.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x21_-_Todo_Mundo_Odeia_O_Dia_das_Mães.mp4',
					'genre': ''},

					{'name': '3x22_-_todo_mundo_odeia_a_formatura',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/3x22_-_todo_mundo_odeia_a_formatura.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/3x22_-_todo_mundo_odeia_a_formatura.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/3x22_-_Todo_Mundo_Odeia_A_Formatura.mp4',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e01.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e01.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e01.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E01.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e02.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e02.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e02.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E02.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e03.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e03.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e03.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E03.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e04.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e04.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e04.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E04.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e05.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e05.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e05.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E05.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e06.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e06.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e06.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E06.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e07.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e07.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e07.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E07.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e08.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e08.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e08.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E08.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e09.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e09.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e09.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E09.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e10.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e10.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e10.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E10.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e11.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e11.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e11.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E11.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e12.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e12.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e12.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E12.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e13.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e13.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e13.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E13.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e14.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e14.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e14.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E14.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e15.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e15.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e15.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E15.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e16.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e16.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e16.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E16.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e17.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e17.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e17.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E17.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e18.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e18.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e18.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E18.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e19.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e19.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e19.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E19.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e20.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e20.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e20.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E20.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e21.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e21.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e21.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E21.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t01e22.web-dl.720p.dublado_-_www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e22.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t01e22.web-dl.720p.dublado_-_www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T01E22.WEB-DL.720p.Dublado_-_WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e01.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e01.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e01.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E01.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e02.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e02.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e02.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E02.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e03.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e03.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e03.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E03.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e04.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e04.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e04.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E04.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e05.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e05.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e05.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E05.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e06.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e06.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e06.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E06.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e07.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e07.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e07.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E07.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e08.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e08.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e08.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E08.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e09.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e09.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e09.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E09.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e10.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e10.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e10.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E10.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e11.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e11.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e11.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E11.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e12.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e12.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e12.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E12.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e13.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e13.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e13.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E13.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e14.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e14.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e14.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E14.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e15.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e15.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e15.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E15.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e16.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e16.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e16.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E16.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e17.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e17.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e17.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E17.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e18.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e18.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e18.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E18.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e19.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e19.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e19.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E19.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e20.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e20.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e20.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E20.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e21.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e21.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e21.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E21.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

					{'name': 'todo.mundo.odeia.o.chris.t04e22.web-dl.720p.dublado.www.torrrentdosfilmes.com',
					'fanart':'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e22.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'thumb': 'http://192.168.0.10:8080/midias/Series/img/todo.mundo.odeia.o.chris.t04e22.web-dl.720p.dublado.www.torrrentdosfilmes.com.jpg',
					'video': 'http://192.168.0.10:8080/midias/Series/Todo.Mundo.Odeia.o.Chris.T04E22.WEB-DL.720p.Dublado.WWW.TORRRENTDOSFILMES.COM.mkv',
					'genre': ''},

]}

def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: types.GeneratorType
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'minha coleção')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['fanart']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # https://codedocs.xyz/xbmc/xbmc/group__python__xbmcgui__listitem.html#ga0b71166869bda87ad744942888fb5f14
        # 'mediatype' is needed for a skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': category,
                                    'genre': category,
                                    'mediatype': 'video'})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        # 'mediatype' is needed for skin to display info for this ListItem correctly.
        list_item.setInfo('video', {'title': video['name'],
                                    'genre': video['genre'],
                                    'mediatype': 'video'})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['fanart']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
