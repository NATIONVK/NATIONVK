<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="assets/css/style.css" />
    <link
      href="https://fonts.googleapis.com/css?family=Kaushan+Script|Montserrat:300i,400,700&amp;subset=cyrillic-ext"
      rel="stylesheet"
    />
    <link
      rel="stylesheet"
      href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
      integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr"
      crossorigin="anonymous"
    />
    <link
      rel="stylesheet"
      type="text/css"
      href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"
    />
    <title>NATION VK</title>
  </head>
  <body>
    <header class="header" id="header">
      <div class="container">
        <div class="header__inner">
          <div class="header__logo" data-scroll="#intro">BlackBerry</div>

          <nav class="nav" id="nav">
            <a class="nav__link" href="#" data-scroll="#about">About</a>
            <a class="nav__link" href="#" data-scroll="#services">Service</a>
            <a class="nav__link" href="#" data-scroll="#blog">Blog</a>
            <a class="nav__link" href="#" data-scroll="#works">Work</a>
            <a class="nav__link" href="#" data-scroll="#footer">Contact</a>
            <a class="nav__link" href="#">
              <i class="fas fa-shopping-cart"></i>
            </a>
            <a class="nav__link" href="#">
              <i class="fas fa-search"></i>
            </a>
          </nav>

          <button class="nav-toggle" id="nav_toggle" type="button">
            <span class="nav-toggle__item">Menu</span>
          </button>
        </div>
      </div>
    </header>

    <div class="page">
      <!-- Шапка -->
      <div class="intro" id="intro">
        <div class="container">
          <div class="intro__inner">
            <h2 class="intro__suptitle">Creative Template</h2>
            <h1 class="intro__title">Welcome to BlackBerry</h1>

            <a class="btn" href="#">Learn More</a>
          </div>
        </div>
      </div>

      <!-- О нас -->
      <section class="section" id="about">
        <div class="container">
          <div class="section__header">
            <h3 class="section__suptitle">What we do</h3>
            <h2 class="section__title">Story about us</h2>
            <div class="section__text">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat.
              </p>
            </div>
          </div>

          <div class="card">
            <div class="card__item">
              <div class="card__inner">
                <div class="card__img">
                  <img src="assets/images/about/1.jpg" alt="" />
                </div>
              </div>
            </div>

            <div class="card__item">
              <div class="card__inner">
                <div class="card__img">
                  <img src="assets/images/about/2.jpg" alt="" />
                </div>
              </div>
            </div>

            <div class="card__item">
              <div class="card__inner">
                <div class="card__img">
                  <img src="assets/images/about/3.jpg" alt="" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Статистика -->
      <div class="statistics">
        <div class="container">
          <div class="stat">
            <div class="stat__item">
              <div class="stat__count">42</div>
              <div class="stat__text">Web Design Projects</div>
            </div>
            <div class="stat__item">
              <div class="stat__count">123</div>
              <div class="stat__text">happy client</div>
            </div>
            <div class="stat__item">
              <div class="stat__count">15</div>
              <div class="stat__text">award winner</div>
            </div>
            <div class="stat__item">
              <div class="stat__count">99</div>
              <div class="stat__text">cup of coffee</div>
            </div>
            <div class="stat__item">
              <div class="stat__count">24</div>
              <div class="stat__text">members</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Услуги -->
      <section class="section" id="services">
        <div class="container">
          <div class="section__header">
            <h3 class="section__suptitle">We work with</h3>
            <h2 class="section__title">Amazing Services</h2>
          </div>

          <div class="services">
            <div class="services__item services__item--border">
              <img
                class="services__icon"
                src="assets/images/services/photography.png"
                alt=""
              />

              <div class="services__title">Photography</div>
              <div class="services__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor.
              </div>
            </div>
            <div class="services__item services__item--border">
              <img
                class="services__icon"
                src="assets/images/services/webdesign.png"
                alt=""
              />

              <div class="services__title">Web Design</div>
              <div class="services__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor.
              </div>
            </div>
            <div class="services__item services__item--border">
              <img
                class="services__icon"
                src="assets/images/services/creativity.png"
                alt=""
              />

              <div class="services__title">Creativity</div>
              <div class="services__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor.
              </div>
            </div>
            <div class="services__item">
              <img
                class="services__icon"
                src="assets/images/services/seo.png"
                alt=""
              />

              <div class="services__title">seo</div>
              <div class="services__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor.
              </div>
            </div>
            <div class="services__item">
              <img
                class="services__icon"
                src="assets/images/services/css-html.png"
                alt=""
              />

              <div class="services__title">Css/Html</div>
              <div class="services__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor.
              </div>
            </div>
            <div class="services__item">
              <img
                class="services__icon"
                src="assets/images/services/digital.png"
                alt=""
              />

              <div class="services__title">digital</div>
              <div class="services__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor.
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Цитата 1 -->
      <div class="section section--gray">
        <div class="container">
          <div class="reviews">
            <div data-slider>
              <div>
                <div class="reviews__item">
                  <img
                    class="reviews__photo"
                    src="assets/images/avatar.png"
                    alt=""
                  />
                  <div class="reviews__text">
                    “Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                    sed do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation.”
                  </div>
                  <div class="reviews__author">Jon Doe</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Команда -->
      <section class="section">
        <div class="container">
          <div class="section__header">
            <h3 class="section__suptitle">Who we are</h3>
            <h2 class="section__title">Meet our team</h2>
            <div class="section__text">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat.
              </p>
            </div>
          </div>

          <div class="card">
            <div class="card__item">
              <div class="card__inner">
                <div class="card__img">
                  <img src="assets/images/team/1.jpg" alt="" />
                </div>
                <div class="card__text"></div>
              </div>
              <div class="card__info">
                <div class="card__name">Matthew Dix</div>
                <div class="card__prof">Graphic Design</div>
              </div>
            </div>

            <div class="card__item">
              <div class="card__inner">
                <div class="card__img">
                  <img src="assets/images/team/2.jpg" alt="" />
                </div>
                <div class="card__text"></div>
              </div>
              <div class="card__info">
                <div class="card__name">Christopher Campbell</div>
                <div class="card__prof">Branding/UX design</div>
              </div>
            </div>

            <div class="card__item">
              <div class="card__inner">
                <div class="card__img">
                  <img src="assets/images/team/3.jpg" alt="" />
                </div>
                <div class="card__text"></div>
              </div>
              <div class="card__info">
                <div class="card__name">Michael Fertig</div>
                <div class="card__prof">Developer</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Награды -->
      <div class="section section--gray">
        <div class="container">
          <div class="logos">
            <div class="logos__item">
              <img class="logos__img" src="assets/images/logos/1.png" alt="" />
            </div>
            <div class="logos__item">
              <img class="logos__img" src="assets/images/logos/2.png" alt="" />
            </div>
            <div class="logos__item">
              <img class="logos__img" src="assets/images/logos/3.png" alt="" />
            </div>
            <div class="logos__item">
              <img class="logos__img" src="assets/images/logos/4.png" alt="" />
            </div>
            <div class="logos__item">
              <img class="logos__img" src="assets/images/logos/5.png" alt="" />
            </div>
            <div class="logos__item">
              <img class="logos__img" src="assets/images/logos/6.png" alt="" />
            </div>
          </div>
        </div>
      </div>

      <!-- Работы -->
      <section class="section" id="works">
        <div class="container">
          <div class="section__header">
            <h3 class="section__suptitle">What we do</h3>
            <h2 class="section__title">some of our work</h2>
            <div class="section__text">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat.
              </p>
            </div>
          </div>
        </div>

        <div class="works">
          <div class="works__col">
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/1.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/2.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
          </div>

          <div class="works__col">
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/3.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/4.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
          </div>

          <div class="works__col">
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/5.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
          </div>

          <div class="works__col">
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/6.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/7.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
          </div>
        </div>
      </section>

      <!-- Цитата 2 -->
      <div class="section">
        <div class="container">
          <div class="reviews">
            <div data-slider>
              <div>
                <div class="reviews__item">
                  <img
                    class="reviews__photo"
                    src="assets/images/avatar.png"
                    alt=""
                  />
                  <div class="reviews__text">
                    “Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                    sed do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation.”
                  </div>
                  <div class="reviews__author">Jon Doe</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Clients -->
      <section class="section section--clients">
        <div class="container">
          <div class="section__header">
            <h3 class="section__suptitle">Happy Clients</h3>
            <h2 class="section__title">What people say</h2>
          </div>

          <div class="clients">
            <div class="clients__item">
              <img
                class="clients__photo"
                src="assets/images/clients/1.png"
                alt=""
              />
              <div class="clients__content">
                <div class="clients__name">Matthew Dix</div>
                <div class="clients__prof">Graphic Design</div>
                <div class="clients__text">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim.
                </div>
              </div>
            </div>

            <div class="clients__item">
              <img
                class="clients__photo"
                src="assets/images/clients/2.png"
                alt=""
              />
              <div class="clients__content">
                <div class="clients__name">Nick Karvounis</div>
                <div class="clients__prof">Graphic Design</div>
                <div class="clients__text">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim.
                </div>
              </div>
            </div>

            <div class="clients__item">
              <img
                class="clients__photo"
                src="assets/images/clients/3.png"
                alt=""
              />
              <div class="clients__content">
                <div class="clients__name">Jaelynn Castillo</div>
                <div class="clients__prof">Graphic Design</div>
                <div class="clients__text">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim.
                </div>
              </div>
            </div>

            <div class="clients__item">
              <img
                class="clients__photo"
                src="assets/images/clients/4.png"
                alt=""
              />
              <div class="clients__content">
                <div class="clients__name">Mike Petrucci</div>
                <div class="clients__prof">Graphic Design</div>
                <div class="clients__text">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim.
                </div>
              </div>
            </div>
          </div>
          <!-- /.clients -->
        </div>
        <!-- /.container -->
      </section>

      <!-- Blog -->
      <section class="section" id="blog">
        <div class="container">
          <div class="section__header">
            <h3 class="section__suptitle">Our stories</h3>
            <h2 class="section__title">Latest blog</h2>
          </div>

          <div class="blog">
            <div class="blog__item">
              <div class="blog__header">
                <a href="#">
                  <img
                    class="blog__photo"
                    src="assets/images/blog/1.jpg"
                    alt=""
                  />
                </a>
                <div class="blog__date">
                  <div class="blog__date-day">15</div>
                  Jan
                </div>
              </div>
              <div class="blog__content">
                <div class="blog__title">
                  <a href="#">Lorem ipsum dolor sit amet</a>
                </div>
                <div class="blog__text">
                  Consectetur adipiscing elit, sed do eiusmod tempor incididunt
                  ut labore et dolore magna aliqua.
                </div>
              </div>
              <div class="blog__footer">
                <div class="blog-stat">
                  <span class="blog-stat__item">
                    <i class="far fa-eye"></i> 542
                  </span>
                  <span class="blog-stat__item">
                    <i class="far fa-comment-dots"></i> 17
                  </span>
                </div>
              </div>
            </div>

            <div class="blog__item">
              <div class="blog__header">
                <a href="#">
                  <img
                    class="blog__photo"
                    src="assets/images/blog/2.jpg"
                    alt=""
                  />
                </a>
                <div class="blog__date">
                  <div class="blog__date-day">15</div>
                  Jan
                </div>
              </div>
              <div class="blog__content">
                <div class="blog__title">
                  <a href="#">Lorem ipsum dolor sit amet</a>
                </div>
                <div class="blog__text">
                  Consectetur adipiscing elit, sed do eiusmod tempor incididunt
                  ut labore et dolore magna aliqua.
                </div>
              </div>
              <div class="blog__footer">
                <div class="blog-stat">
                  <span class="blog-stat__item">
                    <i class="far fa-eye"></i> 542
                  </span>
                  <span class="blog-stat__item">
                    <i class="far fa-comment-dots"></i> 17
                  </span>
                </div>
              </div>
            </div>

            <div class="blog__item">
              <div class="blog__header">
                <a href="#">
                  <img
                    class="blog__photo"
                    src="assets/images/blog/3.jpg"
                    alt=""
                  />
                </a>
                <div class="blog__date">
                  <div class="blog__date-day">15</div>
                  Jan
                </div>
              </div>
              <div class="blog__content">
                <div class="blog__title">
                  <a href="#">Lorem ipsum dolor sit amet</a>
                </div>
                <div class="blog__text">
                  Consectetur adipiscing elit, sed do eiusmod tempor incididunt
                  ut labore et dolore magna aliqua.
                </div>
              </div>
              <div class="blog__footer">
                <div class="blog-stat">
                  <span class="blog-stat__item">
                    <i class="far fa-eye"></i> 542
                  </span>
                  <span class="blog-stat__item">
                    <i class="far fa-comment-dots"></i> 17
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer class="footer" id="footer">
        <div class="container">
          <div class="footer__inner">
            <div class="footer__col footer__col--first">
              <div class="footer__logo">BlackBerry</div>
              <div class="footer__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat.
              </div>

              <div class="footer__social">
                <div class="footer__social-header"><b>15k</b> followers</div>
                <div class="footer__social-content">
                  Follow Us:
                  <a href="#" target="_blank">
                    <i class="fab fa-facebook"></i>
                  </a>
                  <a href="#" target="_blank">
                    <i class="fab fa-twitter"></i>
                  </a>
                  <a href="#" target="_blank">
                    <i class="fab fa-instagram"></i>
                  </a>
                </div>
              </div>
            </div>

            <div class="footer__col footer__col--second">
              <div class="footer__title">Blogs</div>

              <div class="blogs">
                <div class="blogs__item">
                  <img
                    class="blogs__img"
                    src="assets/images/blog/1.jpg"
                    alt=""
                  />
                  <div class="blogs__content">
                    <a class="blogs__title" href="#"
                      >Lorem ipsum dolor sit amet, consectetur adipiscing</a
                    >
                    <div class="blogs__date">Jan 9, 2016</div>
                  </div>
                </div>

                <div class="blogs__item">
                  <img
                    class="blogs__img"
                    src="assets/images/blog/2.jpg"
                    alt=""
                  />
                  <div class="blogs__content">
                    <a class="blogs__title" href="#">Lorem ipsum dolor</a>
                    <div class="blogs__date">Jan 9, 2016</div>
                  </div>
                </div>

                <div class="blogs__item">
                  <img
                    class="blogs__img"
                    src="assets/images/blog/3.jpg"
                    alt=""
                  />
                  <div class="blogs__content">
                    <a class="blogs__title" href="#"
                      >Lorem ipsum dolor sit amet, consectetur adipiscing</a
                    >
                    <div class="blogs__date">Jan 9, 2016</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="footer__col footer__col--third">
              <div class="footer__title">Instagram</div>

              <div class="instagram">
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/1.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/2.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/3.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/4.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/5.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/6.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/7.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/8.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/9.jpg" alt="" />
                </a>
              </div>
            </div>
          </div>

          <div class="copyright">
            © 2022 PRO NATION<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="assets/css/style.css" />
    <link
      href="https://fonts.googleapis.com/css?family=Kaushan+Script|Montserrat:300i,400,700&amp;subset=cyrillic-ext"
      rel="stylesheet"
    />
    <link
      rel="stylesheet"
      href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
      integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr"
      crossorigin="anonymous"
    />
    <link
      rel="stylesheet"
      type="text/css"
      href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"
    />
    <title>NATION VK</title>
  </head>
  <body>
    <header class="header" id="header">
      <div class="container">
        <div class="header__inner">
          <div class="header__logo" data-scroll="#intro">BlackBerry</div>

          <nav class="nav" id="nav">
            <a class="nav__link" href="#" data-scroll="#about">About</a>
            <a class="nav__link" href="#" data-scroll="#services">Service</a>
            <a class="nav__link" href="#" data-scroll="#blog">Blog</a>
            <a class="nav__link" href="#" data-scroll="#works">Work</a>
            <a class="nav__link" href="#" data-scroll="#footer">Contact</a>
            <a class="nav__link" href="#">
              <i class="fas fa-shopping-cart"></i>
            </a>
            <a class="nav__link" href="#">
              <i class="fas fa-search"></i>
            </a>
          </nav>

          <button class="nav-toggle" id="nav_toggle" type="button">
            <span class="nav-toggle__item">Menu</span>
          </button>
        </div>
      </div>
    </header>

    <div class="page">
      <!-- Шапка -->
      <div class="intro" id="intro">
        <div class="container">
          <div class="intro__inner">
            <h2 class="intro__suptitle">Creative Template</h2>
            <h1 class="intro__title">Welcome to BlackBerry</h1>

            <a class="btn" href="#">Learn More</a>
          </div>
        </div>
      </div>

      <!-- О нас -->
      <section class="section" id="about">
        <div class="container">
          <div class="section__header">
            <h3 class="section__suptitle">What we do</h3>
            <h2 class="section__title">Story about us</h2>
            <div class="section__text">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat.
              </p>
            </div>
          </div>

          <div class="card">
            <div class="card__item">
              <div class="card__inner">
                <div class="card__img">
                  <img src="assets/images/about/1.jpg" alt="" />
                </div>
              </div>
            </div>

            <div class="card__item">
              <div class="card__inner">
                <div class="card__img">
                  <img src="assets/images/about/2.jpg" alt="" />
                </div>
              </div>
            </div>

            <div class="card__item">
              <div class="card__inner">
                <div class="card__img">
                  <img src="assets/images/about/3.jpg" alt="" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Статистика -->
      <div class="statistics">
        <div class="container">
          <div class="stat">
            <div class="stat__item">
              <div class="stat__count">42</div>
              <div class="stat__text">Web Design Projects</div>
            </div>
            <div class="stat__item">
              <div class="stat__count">123</div>
              <div class="stat__text">happy client</div>
            </div>
            <div class="stat__item">
              <div class="stat__count">15</div>
              <div class="stat__text">award winner</div>
            </div>
            <div class="stat__item">
              <div class="stat__count">99</div>
              <div class="stat__text">cup of coffee</div>
            </div>
            <div class="stat__item">
              <div class="stat__count">24</div>
              <div class="stat__text">members</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Услуги -->
      <section class="section" id="services">
        <div class="container">
          <div class="section__header">
            <h3 class="section__suptitle">We work with</h3>
            <h2 class="section__title">Amazing Services</h2>
          </div>

          <div class="services">
            <div class="services__item services__item--border">
              <img
                class="services__icon"
                src="assets/images/services/photography.png"
                alt=""
              />

              <div class="services__title">Photography</div>
              <div class="services__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor.
              </div>
            </div>
            <div class="services__item services__item--border">
              <img
                class="services__icon"
                src="assets/images/services/webdesign.png"
                alt=""
              />

              <div class="services__title">Web Design</div>
              <div class="services__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor.
              </div>
            </div>
            <div class="services__item services__item--border">
              <img
                class="services__icon"
                src="assets/images/services/creativity.png"
                alt=""
              />

              <div class="services__title">Creativity</div>
              <div class="services__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor.
              </div>
            </div>
            <div class="services__item">
              <img
                class="services__icon"
                src="assets/images/services/seo.png"
                alt=""
              />

              <div class="services__title">seo</div>
              <div class="services__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor.
              </div>
            </div>
            <div class="services__item">
              <img
                class="services__icon"
                src="assets/images/services/css-html.png"
                alt=""
              />

              <div class="services__title">Css/Html</div>
              <div class="services__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor.
              </div>
            </div>
            <div class="services__item">
              <img
                class="services__icon"
                src="assets/images/services/digital.png"
                alt=""
              />

              <div class="services__title">digital</div>
              <div class="services__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor.
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Цитата 1 -->
      <div class="section section--gray">
        <div class="container">
          <div class="reviews">
            <div data-slider>
              <div>
                <div class="reviews__item">
                  <img
                    class="reviews__photo"
                    src="assets/images/avatar.png"
                    alt=""
                  />
                  <div class="reviews__text">
                    “Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                    sed do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation.”
                  </div>
                  <div class="reviews__author">Jon Doe</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Команда -->
      <section class="section">
        <div class="container">
          <div class="section__header">
            <h3 class="section__suptitle">Who we are</h3>
            <h2 class="section__title">Meet our team</h2>
            <div class="section__text">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat.
              </p>
            </div>
          </div>

          <div class="card">
            <div class="card__item">
              <div class="card__inner">
                <div class="card__img">
                  <img src="assets/images/team/1.jpg" alt="" />
                </div>
                <div class="card__text"></div>
              </div>
              <div class="card__info">
                <div class="card__name">Matthew Dix</div>
                <div class="card__prof">Graphic Design</div>
              </div>
            </div>

            <div class="card__item">
              <div class="card__inner">
                <div class="card__img">
                  <img src="assets/images/team/2.jpg" alt="" />
                </div>
                <div class="card__text"></div>
              </div>
              <div class="card__info">
                <div class="card__name">Christopher Campbell</div>
                <div class="card__prof">Branding/UX design</div>
              </div>
            </div>

            <div class="card__item">
              <div class="card__inner">
                <div class="card__img">
                  <img src="assets/images/team/3.jpg" alt="" />
                </div>
                <div class="card__text"></div>
              </div>
              <div class="card__info">
                <div class="card__name">Michael Fertig</div>
                <div class="card__prof">Developer</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Награды -->
      <div class="section section--gray">
        <div class="container">
          <div class="logos">
            <div class="logos__item">
              <img class="logos__img" src="assets/images/logos/1.png" alt="" />
            </div>
            <div class="logos__item">
              <img class="logos__img" src="assets/images/logos/2.png" alt="" />
            </div>
            <div class="logos__item">
              <img class="logos__img" src="assets/images/logos/3.png" alt="" />
            </div>
            <div class="logos__item">
              <img class="logos__img" src="assets/images/logos/4.png" alt="" />
            </div>
            <div class="logos__item">
              <img class="logos__img" src="assets/images/logos/5.png" alt="" />
            </div>
            <div class="logos__item">
              <img class="logos__img" src="assets/images/logos/6.png" alt="" />
            </div>
          </div>
        </div>
      </div>

      <!-- Работы -->
      <section class="section" id="works">
        <div class="container">
          <div class="section__header">
            <h3 class="section__suptitle">What we do</h3>
            <h2 class="section__title">some of our work</h2>
            <div class="section__text">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat.
              </p>
            </div>
          </div>
        </div>

        <div class="works">
          <div class="works__col">
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/1.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/2.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
          </div>

          <div class="works__col">
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/3.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/4.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
          </div>

          <div class="works__col">
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/5.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
          </div>

          <div class="works__col">
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/6.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
            <div class="works__item">
              <img
                class="works__image"
                src="assets/images/works/7.jpg"
                alt=""
              />
              <div class="works__info"></div>
            </div>
          </div>
        </div>
      </section>

      <!-- Цитата 2 -->
      <div class="section">
        <div class="container">
          <div class="reviews">
            <div data-slider>
              <div>
                <div class="reviews__item">
                  <img
                    class="reviews__photo"
                    src="assets/images/avatar.png"
                    alt=""
                  />
                  <div class="reviews__text">
                    “Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                    sed do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation.”
                  </div>
                  <div class="reviews__author">Jon Doe</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Clients -->
      <section class="section section--clients">
        <div class="container">
          <div class="section__header">
            <h3 class="section__suptitle">Happy Clients</h3>
            <h2 class="section__title">What people say</h2>
          </div>

          <div class="clients">
            <div class="clients__item">
              <img
                class="clients__photo"
                src="assets/images/clients/1.png"
                alt=""
              />
              <div class="clients__content">
                <div class="clients__name">Matthew Dix</div>
                <div class="clients__prof">Graphic Design</div>
                <div class="clients__text">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim.
                </div>
              </div>
            </div>

            <div class="clients__item">
              <img
                class="clients__photo"
                src="assets/images/clients/2.png"
                alt=""
              />
              <div class="clients__content">
                <div class="clients__name">Nick Karvounis</div>
                <div class="clients__prof">Graphic Design</div>
                <div class="clients__text">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim.
                </div>
              </div>
            </div>

            <div class="clients__item">
              <img
                class="clients__photo"
                src="assets/images/clients/3.png"
                alt=""
              />
              <div class="clients__content">
                <div class="clients__name">Jaelynn Castillo</div>
                <div class="clients__prof">Graphic Design</div>
                <div class="clients__text">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim.
                </div>
              </div>
            </div>

            <div class="clients__item">
              <img
                class="clients__photo"
                src="assets/images/clients/4.png"
                alt=""
              />
              <div class="clients__content">
                <div class="clients__name">Mike Petrucci</div>
                <div class="clients__prof">Graphic Design</div>
                <div class="clients__text">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
                  do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                  Ut enim ad minim.
                </div>
              </div>
            </div>
          </div>
          <!-- /.clients -->
        </div>
        <!-- /.container -->
      </section>

      <!-- Blog -->
      <section class="section" id="blog">
        <div class="container">
          <div class="section__header">
            <h3 class="section__suptitle">Our stories</h3>
            <h2 class="section__title">Latest blog</h2>
          </div>

          <div class="blog">
            <div class="blog__item">
              <div class="blog__header">
                <a href="#">
                  <img
                    class="blog__photo"
                    src="assets/images/blog/1.jpg"
                    alt=""
                  />
                </a>
                <div class="blog__date">
                  <div class="blog__date-day">15</div>
                  Jan
                </div>
              </div>
              <div class="blog__content">
                <div class="blog__title">
                  <a href="#">Lorem ipsum dolor sit amet</a>
                </div>
                <div class="blog__text">
                  Consectetur adipiscing elit, sed do eiusmod tempor incididunt
                  ut labore et dolore magna aliqua.
                </div>
              </div>
              <div class="blog__footer">
                <div class="blog-stat">
                  <span class="blog-stat__item">
                    <i class="far fa-eye"></i> 542
                  </span>
                  <span class="blog-stat__item">
                    <i class="far fa-comment-dots"></i> 17
                  </span>
                </div>
              </div>
            </div>

            <div class="blog__item">
              <div class="blog__header">
                <a href="#">
                  <img
                    class="blog__photo"
                    src="assets/images/blog/2.jpg"
                    alt=""
                  />
                </a>
                <div class="blog__date">
                  <div class="blog__date-day">15</div>
                  Jan
                </div>
              </div>
              <div class="blog__content">
                <div class="blog__title">
                  <a href="#">Lorem ipsum dolor sit amet</a>
                </div>
                <div class="blog__text">
                  Consectetur adipiscing elit, sed do eiusmod tempor incididunt
                  ut labore et dolore magna aliqua.
                </div>
              </div>
              <div class="blog__footer">
                <div class="blog-stat">
                  <span class="blog-stat__item">
                    <i class="far fa-eye"></i> 542
                  </span>
                  <span class="blog-stat__item">
                    <i class="far fa-comment-dots"></i> 17
                  </span>
                </div>
              </div>
            </div>

            <div class="blog__item">
              <div class="blog__header">
                <a href="#">
                  <img
                    class="blog__photo"
                    src="assets/images/blog/3.jpg"
                    alt=""
                  />
                </a>
                <div class="blog__date">
                  <div class="blog__date-day">15</div>
                  Jan
                </div>
              </div>
              <div class="blog__content">
                <div class="blog__title">
                  <a href="#">Lorem ipsum dolor sit amet</a>
                </div>
                <div class="blog__text">
                  Consectetur adipiscing elit, sed do eiusmod tempor incididunt
                  ut labore et dolore magna aliqua.
                </div>
              </div>
              <div class="blog__footer">
                <div class="blog-stat">
                  <span class="blog-stat__item">
                    <i class="far fa-eye"></i> 542
                  </span>
                  <span class="blog-stat__item">
                    <i class="far fa-comment-dots"></i> 17
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer class="footer" id="footer">
        <div class="container">
          <div class="footer__inner">
            <div class="footer__col footer__col--first">
              <div class="footer__logo">BlackBerry</div>
              <div class="footer__text">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat.
              </div>

              <div class="footer__social">
                <div class="footer__social-header"><b>15k</b> followers</div>
                <div class="footer__social-content">
                  Follow Us:
                  <a href="#" target="_blank">
                    <i class="fab fa-facebook"></i>
                  </a>
                  <a href="#" target="_blank">
                    <i class="fab fa-twitter"></i>
                  </a>
                  <a href="#" target="_blank">
                    <i class="fab fa-instagram"></i>
                  </a>
                </div>
              </div>
            </div>

            <div class="footer__col footer__col--second">
              <div class="footer__title">Blogs</div>

              <div class="blogs">
                <div class="blogs__item">
                  <img
                    class="blogs__img"
                    src="assets/images/blog/1.jpg"
                    alt=""
                  />
                  <div class="blogs__content">
                    <a class="blogs__title" href="#"
                      >Lorem ipsum dolor sit amet, consectetur adipiscing</a
                    >
                    <div class="blogs__date">Jan 9, 2016</div>
                  </div>
                </div>

                <div class="blogs__item">
                  <img
                    class="blogs__img"
                    src="assets/images/blog/2.jpg"
                    alt=""
                  />
                  <div class="blogs__content">
                    <a class="blogs__title" href="#">Lorem ipsum dolor</a>
                    <div class="blogs__date">Jan 9, 2016</div>
                  </div>
                </div>

                <div class="blogs__item">
                  <img
                    class="blogs__img"
                    src="assets/images/blog/3.jpg"
                    alt=""
                  />
                  <div class="blogs__content">
                    <a class="blogs__title" href="#"
                      >Lorem ipsum dolor sit amet, consectetur adipiscing</a
                    >
                    <div class="blogs__date">Jan 9, 2016</div>
                  </div>
                </div>
              </div>
            </div>

            <div class="footer__col footer__col--third">
              <div class="footer__title">Instagram</div>

              <div class="instagram">
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/1.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/2.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/3.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/4.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/5.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/6.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/7.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/8.jpg" alt="" />
                </a>
                <a class="instagram__item" href="#" target="_blank">
                  <img src="assets/images/instagram/9.jpg" alt="" />
                </a>
              </div>
            </div>
          </div>

          <div class="copyright">
            © 2022 BlackBerry free PSD template by <span>Daniel</span>
          </div>
        </div>
      </footer>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script
      type="text/javascript"
      src="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"
    ></script>
    <script src="assets/js/app.js"></script>
  </body>
</html>
 free PSD template by <span>Daniel</span>
          </div>
        </div>
      </footer>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script
      type="text/javascript"
      src="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"
    ></script>
    <script src="assets/js/app.js"></script>
  </body>
</html>
