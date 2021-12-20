import __SocialMedia_Sites as SM
from __SocialMedia_Sites import *
import requests
import time


#

# WEBSITES = [
# instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
# wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus,
# medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
# mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
# goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
# dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
# wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
# contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
# bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp]

def search():
    SM.USERNAME
    print(f'[SYS] Searching For Username: {SM.USERNAME}')
    time.sleep(.05)
    print('*' * 10)
    time.sleep(.05)
    print('*' * 10, '\n')
    print('[SYS] Doing my magic...')
    time.sleep(.05)

    COUNT = 0
    ACCOUNT_STATUS = True

    for url in SM.WEBSITES: ## iterate through WEBSITE list and sent get requests.
        r = requests.get(url) # initialize requests, then check status code. 200 == Account_status True. 
        if r.status_code == 200: # checks requerts, if 200 response then valid profile
            if ACCOUNT_STATUS == True: #
                print(f'[SYS] Accounts Found: ')
                ACCOUNT_STATUS = False
            print(f'[SYS]{url} - {r.status_code} - Response: OK')

            if SM.USERNAME in r.text:
                print(f'[SYS] Account - {SM.USERNAME}) - found in URL')
            else:
                print(f'[SYS]Account - {SM.USERNAME}) - NOT found in URL (Still a match)')
        COUNT += 1
        total = len(WEBSITES) # provide dynamic counter when adding /removing websites
        print(f'[SYS] Found {COUNT} websites the user is a member of out of {total} websites')

if __name__ == '__main__':
    search()




#
