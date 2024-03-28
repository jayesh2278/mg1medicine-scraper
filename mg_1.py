import requests
import json
import string
from apify import Actor

async def main():
    for alpha in list(string.ascii_lowercase):
        url = "https://www.1mg.com/pharmacy_api_gateway/v4/drug_skus/by_prefix?prefix_term="+alpha+"&page=1&per_page=30"
        payload={}
        headers = {
        'authority': 'www.1mg.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8,gu;q=0.7',
        'cache-control': 'no-cache, no-store, must-revalidate',
        'cookie': 'VISITOR-ID=f8e0ea3c-2edf-4484-c451-4c270bcbda41_acce55_1651173890; city=New%20Delhi; abVisitorId=726518; abExperimentShow=false; _csrf=NWNDXzHTMP5UI6cEMWBQngif; isLocaleRedirect=false; isLocaleUIChange=false; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19YDaQ4PVlvJanqxW%2FeTQJa2t2C22nD70avrA0x2G4FR1eIQ9Nnyuzx; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2BvUrtboVZWHdBlvDcq%2F5h1yhMzcr0PihYKpT18j6yifBaYI3K2iFOE; geolocation=false; session=S4CrOUePEodYXjqpfwREsg.fx73NSV3fNPL9mojFdM6yhnsad2TlMazXhRmrNDnZWqq9eJA7LzWckS20jLXji6XWZDUFhSkwjNWlj88P-OWvD58LRFJGlYy1iak9mjqhPWMPfdl15yYf4wshOqL_TnzkgmfPb_ZkyxtpG1p3w5MGA.1651173894147.2592000000.3v5vn_2_i9H75QYqyr0o8L2HCUQa6cM6VcbwlXYz1X0; _gcl_au=1.1.2059234815.1651173894; _fbp=fb.1.1651173894489.1460713567; MgidSensorNVis=1; MgidSensorHref=https://www.1mg.com/; _nv_did=173339004.1651173895.2402:3a80:809:8459:45e9:dad8:2b48:4c7fxnwqh; __gads=ID=d8318dec40026fab:T=1651173895:S=ALNI_MbNomF-HVVhOOpl8RePUDLRZ3Txig; _ga=GA1.2.1511574528.1651173895; _gid=GA1.2.2009573568.1651173896; singular_device_id=3a8d0c40-5ba5-4ce8-bcfc-030e61674fdb; __adroll_fpc=99e61afab58a9b4d48247eb338f79bc0-1651173896585; nvpush_overlay=1; _nv_push_error=201; amoSessionId=20c1f23c-d7ce-4859-88ec-cce0b2dacee8; _nv_sess=173339004.1651204998.jHooH9aFzz481fbRl6ij4VmhGipDKmv3xZGlDnCz5FbH2oa8ML; _nv_uid=173339004.1651173895.1f2ce7ba-9ef3-4988-a00f-2b04520ce49b.1651173895.1651204998.2.0; _nv_utm=173339004.1651173895.2.1.dXRtc3JjPWdvb2dsZXx1dG1jY249KG5vdCBzZXQpfHV0bWNtZD1vcmdhbmljfHV0bWN0cj0obm90IHByb3ZpZGVkKXx1dG1jY3Q9KG5vdCBzZXQpfGdjbGlkPShub3Qgc2V0KQ==; AMP_TOKEN=%24NOT_FOUND; __gpi=UID=00000511d5cfd682:T=1651173895:RT=1651205000:S=ALNI_MZSylfu9XX03b1zvl6ZkXKLw0Tgjg; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2BsPI5ANqYrioq4%2FBAHPo8ihTxBu2Ka5sE%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX19FfmI%2BXykRRrl2B05e26wiF2FvMMjS5kk%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19g86CTLdxtLw3ZU1skd9aKHCJeeLQwie0QiaPy1%2BbBXKBdXeatvxVjNUFWI6VvUGxxEt8gfwzXcA%3D%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2FQ%2BysMcGymRfHZgf0VeelWBBJ5FCcEwTfJUdW1elwGVe6dC4FBgOekhKEyHqxLaO0nB9Ad7dpNYb0oiDZWpAWxs%2F6n%2BjS%2B2j4%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2BnV%2BpXTey3EUFTqHKTD9Wd3Rh1A4qy%2BAZkF7wL%2BphQQVXbnaL7DNy7lwe0iT9TKIl0wwz3AXOgnw%3D%3D; _uetsid=e1d896e0c72811ec9441336cc8c11883; _uetvid=e1d8e630c72811eca4bde78465ae534e; _nv_hit=173339004.1651205101.cHZpZXc9NA==; __ar_v4=U4ZFS2QH4VB65A54O43AEQ%3A20220428%3A9%7C6PFMKMAZXFGFLMSXPCJHFF%3A20220428%3A9%7CKJTLL7NSNRFA5J3GVYGJVJ%3A20220428%3A9; _gat_UA-21820217-6=1',
        'dnt': '1',
        'hkp-platform': 'Healthkartplus-0.0.1-Desktop',
        'pragma': 'no-cache',
        'referer': 'https://www.1mg.com/drugs-all-medicines?label=c',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'x-csrf-token': 'OL02BBtT-FnGKOUqvPxHCbLlEY5gyzdGXApo',
        'x-html-canrender': 'True',
        'x-platform': 'Desktop-0.0.1'
        }
        
        response = requests.request("GET", url, headers=headers, data=payload)
        
        
        datas = json.loads(response.text)
        sku = datas['data']['skus']
        for sk in sku:
            name = sk['manufacturer_name']
            print(name)

  
