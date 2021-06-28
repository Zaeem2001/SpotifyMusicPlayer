#JUST STORES INFORMATION NEEDED TO ACCESS SPOTIFY, NO LONGER NEEDED

#Client ID 406dbe7264234e59824f91aa3fdebbb8
#Client Secret 29a8cfa566764814a1929cddae262a8

# AUTHORIZATION REQUEST (client ID, response type, redirect uri, scope)
#https://accounts.spotify.com/authorize?client_id=406dbe7264234e59824f91aa3fdebbb8&response_type=code&redirect_uri=https%3A%2F%2Fgithub.com%2FZaeem2001&scope=user-modify-playback-state%20user-read-currently-playing%20user-read-playback-state%20playlist-read-private%20playlist-read-collaborative

# GET RESPONSE BACK (above)                              
#curl -H "Authorization: Basic NDA2ZGJlNzI2NDIzNGU1OTgyNGY5MWFhM2ZkZWJiYjg6MjlhOGNmYTU2Njc2NDgxNGExOTI5Y2RkYWUyNjJhODA=" -d grant_type=authorization_code -d code=AQDSKC0kONdzfBtCjyJrHM14kxdBMQZ8PWDaTvdifP2t0YN93svCThxbj_GzmKBvRJyeaEpYvuaW_zXOsAAMBfcmXjbAldGLWdfKaLxpLUF754ZuZZyPe_t5XWZpJiaA7fgkv8R9CtTnQSBgmDAagX1hNVTc4lcbRl2gFHsz3IM3DeoM-KMrctZ-OpbkmcKhlcRWG4xupXTydRVZ6NXpjhhh_d5Z_9Oy2AjhzibSZKcmLWhvQmuh7zLLLGML3OttwHowxA9_AUamlvD3juLN4t6Lh_FD6qFlgyMVqq3DXHekZsOHPBew6ucPtb6-MMsEf0GwTh_WOkBsRmK9T4-lsoEAlpNI6z0 -d redirect_uri=https%3A%2F%2Fgithub.com%2FZaeem2001 https://accounts.spotify.com/api/token --ssl-no-revoke

# ACCESS TOKEN: BQB--cUNMwRkBZpXmw2cGieBo1p_3sBybYDvL3_o17DciUOXK_dUqhcUvHM4wzcNp1sNuaApnAwH3P2Wu9r0iHUqsWA2uYI1q9QvBh4j67uiMILg1SVCGLrMoXVeN5zFuhYO6y66zNWM7QBfCBh6DTzQxFh2rESWAGinajCanA
# REFRESH TOKEN: AQDr060RMsTXy0T2hLbhQ_60u6Qdl58P5JCH1n0WXcX4LFgNHaV7RSUTKPSVpBa7qHXdvkc-OZC6eanTZQxaKDbTy6BN8cIdo1o9cw6qF1El9CRGnIZ7EJl2oRy_MKmU5rk

#spotify_token = "BQAty796ZYYvK2EeyLDxy1u5xdnwzbWGl7qczzq4mXMB7RJ1tVqGaH4J69Cj1XuP8oCB3YfGAkUmqPncceXvia2MF-aZfgGV4zbmLAhzs_gnlVyoR3nCmQ1Iz-sxntST22o4CW62ATMWGxvhzDHR9LdOD79i"
user_id = "zaeemghauri"
refresh_token = "AQDr060RMsTXy0T2hLbhQ_60u6Qdl58P5JCH1n0WXcX4LFgNHaV7RSUTKPSVpBa7qHXdvkc-OZC6eanTZQxaKDbTy6BN8cIdo1o9cw6qF1El9CRGnIZ7EJl2oRy_MKmU5rk"
base_64 = "NDA2ZGJlNzI2NDIzNGU1OTgyNGY5MWFhM2ZkZWJiYjg6MjlhOGNmYTU2Njc2NDgxNGExOTI5Y2RkYWUyNjJhODA="
