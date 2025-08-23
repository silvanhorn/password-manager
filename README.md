# Password generator

This project is supposed to be a side project. I learned a lot while building that application and still have many ideas
on how to improve this project.

## good to know

This application only works local on your pc.
That means, that there are no external servers doing stuff.

## tips while using this password generator

We recommend using at least 10 character long passwords.
The genertor won't accept a number below 5.

## How does it work?

The Generator has multiple functions. 

### Generating the password

I think the main function of the this program is generating the passwords


# How to use it

One of the maingoal when we were building this project was to make it easy to use.
So its pretty easy to execute this programm.

```bash
git clone gitlab.com/silvanhorn/password-generator
```

```
cd password-generator
```

```
python main.py
```

Once you started the app, I think its pretty self explaining.
You can enter the wished length of your password to field.
Then you can press submit.

Now a second window will appear. This window shows the generated password.
Now you have multiple options. You could eiter copy it into your clipboard or save it into the built-in database.

For both of those options there are buttons.

If you decide to save the generated password by clicking the button, a new window will open the password is already
shown there. Now you have to fill out a form containing information like the username and the service, to which
the password belongs to.

If you are finished with that, you could submit by simply clicking the "submit" button.

Now the password is saved as a hash value into a local database.

Also to mention is, that for every importan feature there are also keybinding:

Enter: submit length and generate password

Weitere folgen


## Thanksayings 

I want to thank to Daniel Miessler, who maintains the repository in which the list of the passowords is hosted. 
It was really helpful to use them in my project aand I am grateful. 

##Credits

Daniel Miessler - github: https://github.com/danielmiessler


