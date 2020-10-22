from app import db, Post, User

if False:  # __name__ == '__main__':
    print(User.query.all())

if __name__ == '__main__':
    db.create_all()
    hello_post = Post(title='Hello')
    bye_post = Post(title='Bye')
    seeyou_post = Post(title='See you')
    user_kelvin = User(name='kelvin', post=hello_post)
    user_andrew = User(name='andrew', post=bye_post)
    user_michael = User(name='michael', post=seeyou_post)

    db.session.add_all([hello_post, bye_post, seeyou_post,
                        user_kelvin, user_andrew, user_michael])
    print(hello_post.userid)
    # db.session.add(hello_post)
    # db.session.add(bye_post)
    # db.session.add(seeyou_post)
    # db.session.add(user_kelvin)
    # db.session.add(user_andrew)
    # db.session.add(user_michael)
    db.session.commit()
    print(hello_post.userid)

    print(Post.query.all())
    print(User.query.all())

    # joined = User.query.join(Post)
    #     .add_columns(User.id, User.username, User.role_id, Role.name)
    #     .filter(User.role_id == Role.id).all()
    # print(joined)