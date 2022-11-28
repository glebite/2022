l_outlets = "@cnbc @cbsnews @msnbc @time @nbcnews @CTVNews @nytimes @washingtonpost @BBCBreaking @BBCWorld @FoxNews @guardiannews @Reuters @euronews @SkyNews @globalnews @CNN @CBCNews @60Minutes @nytpolitics @politico @FRANCE24 @Telegraph @ABC @enews @ANI @aljazeeraenglish @UN_HRC @hrw @UN @UNICEF @UNHumanRights @hrw @UNOCHA @amnesty @amnestyusa @AmnestyIran @UNICEF @EU_Commission @AgnesCallamard @volker_turk @antonioguterres @catherinerusse2 @KenRoth @WHO"

message = """#Arash_Sadeghi, a human rights activist in Iran has been wrongfully arrested with thousands of others.  He is battling cancer but has been denied access to his life-saving medical treatments.  Action is needed now to save his life!

#آرش_صادقی
#مهسا_امینی
"""

for outlet in l_outlets.split(' '):
    output = f'{outlet} {message}'
    print(output)
