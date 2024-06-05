<!-- markdownlint-disable -->
# iStatus 🏷️

Welcome to iStatus, with iStatus, you can utilize Lanyard to display your current Discord Status on your GitHub Profile with one request.

Join our Discord: https://discord.gg/ysjEav7pAV

## Usage

1.) Join the Lanyard [Discord](https://discord.com/invite/WScAm7vNGF) server if you haven't.

2.) Inside a **README.md** file, insert the following with replacing :id with your Discord ID:
```md
<img src="https://lanyard-istatus.vercel.app/user_status/:id" height=":height" width=":width">
```
It should display something somewhat like to this:

<img src="https://lanyard-istatus.vercel.app/user_status/1144267370769174608?type=normal" height="30" width="75"> or <img src="https://lanyard-istatus.vercel.app/user_status/1144267370769174608?type=circled" height="30" width="30">

## Options

There is only currently **one** option that can be used in our API.

### _Type_
Append the query parameter `type=:type` to the end of the URL replacing :type.

```https://lanyard-istatus.vercel.app/user_status/:id?type=normal```
