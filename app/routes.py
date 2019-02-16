from flask import render_template,redirect,url_for,flash
from app import website,db
from flask_login import current_user,login_user,logout_user
from app.models import User,Post
from app.mail import send_email
from app.forms import EmailForm,SignupForm,LoginForm,BlogForm


@website.route('/')
@website.route('/home',methods= ['GET', 'POST'])
def home():
    form = EmailForm()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            return redirect(url_for('logout'))
    else:
        if form.validate_on_submit():
            return redirect(url_for('signup'))
    return render_template('home.html',form=form)

@website.route('/signup')
@website.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        db.session.add(user)
        db.session.flush()
        login_user(user)
        return redirect(url_for('home'))
    return render_template('sign_up.html',form=form)


@website.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@website.route('/login')
@website.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        print(current_user,"not working")
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('Invalid username')
            return redirect(url_for('login'))
        login_user(user)#, remember=form.remember_me.data)
        return redirect(url_for('home'))
    return render_template('login.html', form=form)


@website.route('/biography')
def biography():
    return(render_template('biography.html'))

@website.route('/shop')
@website.route('/shop',methods=['GET','POST'])
def shop():
    form = BlogForm()
  #  topics = Post(topic_id=0)
   # db.session.add(topics)
    #db.session.commit()
    posts = Post.query.all()
    if form.validate_on_submit():
      #  print(current_user)
        post = Post(body=form.post.data, author=current_user)#.username)
        posts = Post.query.all()
        for p in posts:
            print(p.author.username)
        db.session.add(post)
        db.session.commit()
     #   a = Post.query.order_by(Post.topic_id.desc()).all()
    #    for updated in a:
      #      b = str(updated)
       #     if len(b) > 4:
        #        print("this means it doesn;t work kinda idk")
         #       updated_list.append(updated)
      #  flash('Your post is now live!')
        return redirect(url_for('shop'))
    return render_template('shop.html', form=form, posts=posts)

@website.route('/songs')
def songs():
    return(render_template('songs.html'))




@website.route('/fan_message')
@website.route('/fan_message',methods=['GET','POST'])
def fan_message():
    form=BlogForm()
    topics = Post(topic_id=0)
    db.session.add(topics)
    db.session.flush()
   # a = Post.query.order_by(Post.topic_id.desc()).all()
  #  for updated in a:
    #    b = str(updated)
   #     if len(b) > 4:
  #          print("this means it doesn;t work kinda idk")
 #           updated_list.append(updated)
    #if form.validate_on_submit():
   #     post = Post(body=form.post.data)
  #      db.session.add(post)
 #       db.session.flush()
    #    flash('Your post is now live!')
   #     return redirect(url_for('iframe_popup'))
    return render_template('fan_message.html',form=form)


@website.route('/tour')
def tour():
    return(render_template('tour.html'))

@website.route('/iframe_popup')
@website.route('/iframe_popup',methods=['GET','POST'])
def iframe_popup():
    #form=BlogForm()
    return render_template('iframe_popup.html')#,form=form)

#@website.route('/signup', methods=['GET','POST'])
#def sign_up():
 #   return(render_template('sign_up.html'))