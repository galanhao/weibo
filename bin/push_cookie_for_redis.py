import requests

url = "http://47.98.129.65:8002/cookie_pool/add"

rsp = requests.get(url, params={
    # "cookie": "SINAGLOBAL=7275690382884.49.1618922819947; _ga=GA1.2.826918709.1619252479; UOR=www.google.com.hk,weibo.com,login.sina.com.cn; _s_tentry=-; Apache=9836430982976.916.1619871180733; ULV=1619871180898:12:1:3:9836430982976.916.1619871180733:1619791118657; login_sid_t=529c1c28eddf445af3516c1869ffa93f; cross_origin_proto=SSL; SCF=Aujwfj7crOcHIYayS-xSmG44wofxAMe5D-fp7pMVEAtTevi9JXkP8hXzlknrE0iYSP3Qr-05R_E7ZOEAk16P9Uo.; SUB=_2A25NiT2mDeRhGeNG7loX-CfEzDiIHXVu_yhurDV8PUNbmtANLRTXkW9NSyouyUx24cs3fk1VdQVFYmIHRAeqdNS2; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5WJLIUfr7.Os._AeE2SZj-5JpX5K2hUgL.Fo-RSKnc1h.RS0B2dJLoIpqLxK-LBK-L1-2LxKML1h-LB.BfShM0; ALF=1651409270; SSOLoginState=1619873270; wvr=6; webim_unReadCount=%7B%22time%22%3A1619873329391%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A1%2C%22msgbox%22%3A0%7D",
    # "cookie": "WBtopGlobal_register_version:91c79ed46b5606b9;webim_unReadCount:%7B%22time%22%3A1619879516727%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A6%2C%22msgbox%22%3A0%7D;SINAGLOBAL:5089715415731.933.1619879516359;Apache:5089715415731.933.1619879516359;_s_tentry:-;wb_view_log_5858689874:1920*10801;wvr:6;ALF:1651415501;SUB:_2A25NiRYdDeRhGeNG7loX-CfEzDiIHXVu_wDVrDV8PUNbmtAKLXTckW9NSyouyQgM2tApDgtT60cIFAq4rsZhXVGs;SSOLoginState:1619879501;ULV:1619879516553:1:1:1:5089715415731.933.1619879516359:;SUBP:0033WrSXqPxfM725Ws9jqgMF55529P9D9W5WJLIUfr7.Os._AeE2SZj-5JpX5K2hUgL.Fo-RSKnc1h.RS0B2dJLoIpqLxK-LBK-L1-2LxKML1h-LB.BfShM0;SCF:ApXydK3NUsjvknNEieaIEw179nxnycPZMoCo4WMA1f9_QXGKLjAAooLAVPPJOjki-YvdgenyTlGDlXnBbY8feIE.;",
    "cookie": "WBtopGlobal_register_version:91c79ed46b5606b9;webim_unReadCount:%7B%22time%22%3A1620054382160%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A42%2C%22msgbox%22%3A0%7D;SINAGLOBAL:4623070415360.919.1620054381638;Apache:4623070415360.919.1620054381638;_s_tentry:-;wb_view_log_5858687587:1920*10801;wvr:6;ALF:1651590364;SUB:_2A25NlGEMDeRhGeNG7loX-CnJwzuIHXVu4NXErDV8PUNbmtANLWPakW9NSyojUZoSm1c90DmMAIg7PPfGkaNgobdX;SSOLoginState:1620054364;ULV:1620054381832:1:1:1:4623070415360.919.1620054381638:;SUBP:0033WrSXqPxfM725Ws9jqgMF55529P9D9WWjJD3asiWj_M.LG-CCKcl25JpX5K2hUgL.Fo-RSKnc1hMf1hM2dJLoIpMLxKBLB.eL122LxKMLB-2L1heEeoqcSBtt;SCF:AknokJDReSOFtb4EzNeBvORx2eBiSqHPwq92l_K9U-ENRfULbQxSO8uJ1fPci3HK7ktt69I6dMJcGAce09k25UQ.;",
    "account": "alb7rv@sina.com",
    "password": "ymc321",
    "uid": "test3333",
})
print(rsp.status_code)
print(rsp.text)
