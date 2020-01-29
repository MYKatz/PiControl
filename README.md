# Pi

Software to run on raspberry Pis!!

I think the bands we're using follow the Mifare standard, so the code is implemented to use that. If you're using NTAG2xx or something else this might not work for you and some things may need to be changed.

## Things to consider

- What to do when can't connect to internet
    - Some sort of exponential decay/message queue thing...
    - But what sort of feedback do we give the user - yellow light??
- Updating settings
    - We want the pi to constantly be polling the web server to get new settings, etc.
    - Or do we? I guess most core settings will be on the server itself
    - Might still be necessary for stuff that has to do with hardware (ie light color.. etc)
    - If we are implementing this, will need to do it in a way that doesn't interrupt the main thread; check out threading
- Storing settings
    - Will be using pickleDB, a lightweight key-val store

## Installing stuff

pip install package && pip freeze > requirements.txt

