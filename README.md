# Web Crawling Project

Project developed for getting products info from Amazon page.
Firefox browser.

## Installing / Getting started

Installing the necessary dependencies and runs the application:

```shell
$ pip install ipython

$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Developing

### Built With

- python (3.9.0)
- beautifulsoup4 (4.9.3)
- selenium (3.141.0)
- geckodriver (0.28.0)

### Setting up Dev

Using the Bot class:

```shell
$ source venv/bin/activate
$ ipython
$ from core.amazon import Bot
bot = Bot()
bot.search('echo dot')
bot.get_items_search()
```

Returns:

It retuns a list with products title, price and url.

```shell
[{'title': 'Suporte All in one Stand Tomada Amazon Alexa Echo Dot 3 box (branco)',
  'price': 49.9,
  'url': 'https://www.amazon.com.br//Suporte-Stand-Tomada-Amazon-branco/dp/B08H2GKV15/ref=sr_1_23?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=echo+dot&qid=1606652956&sr=8-23'},
 {'title': 'Suporte All in one de Tomada para Amazon Alexa Echo Dot 3 modelo clássico (branco)',
  'price': 54.9,
  'url': 'https://www.amazon.com.br//Suporte-Tomada-Amazon-modelo-cl%C3%A1ssico/dp/B08JSJ5DFR/ref=sr_1_24?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=echo+dot&qid=1606652956&sr=8-24'}]
```
