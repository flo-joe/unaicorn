def fake_predict(user_age):
    if user_age > 10:
        prediction = "survive (over 10)"
    else:
        prediction = "super survive! (10 or under)"
    return prediction