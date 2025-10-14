import httpx

url = "http://127.0.0.1:5000/"

def test_add_subscriber():
    r = httpx.post(url+"add-subscriber",json={"name": "foo", "URI": "somewhere.com"})
    assert(r.status_code == 200)
    r = httpx.post(url+"add-subscriber",json={"name": "bar", "URI": "nowhere.com"})
    assert(r.status_code == 200)
    r = httpx.post(url+"add-subscriber",json={"name": "foobar", "URI": "elsewhere.com"})
    assert(r.status_code == 200)
    r = httpx.post(url+"add-subscriber",json={"name": "bad"})
    assert(r.status_code == 400)
    r = httpx.post(url+"add-subscriber",json={"URI": "beep.com"})
    assert(r.status_code == 400)
    r = httpx.post(url+"add-subscriber",json={})
    assert(r.status_code == 400)

def test_del_subscriber():
    r = httpx.post(url+"del-subscriber",json={"name": "bar"})
    assert(r.status_code == 200)
    r = httpx.post(url+"del-subscriber",json={"name": "no one"})
    assert(r.status_code == 200)
    rdata = r.json()
    assert(rdata.get("message") == "no subscriber named: no one")
    r = httpx.post(url+"del-subscriber",json={})
    assert(r.status_code == 400)

def test_list_subscriber():
    r = httpx.get(url+"list-subscribers")
    rdata = r.json()
    assert(r.status_code == 200)
    assert(rdata.get("foo") == "somewhere.com")
    assert(rdata.get("foobar") == "elsewhere.com")
    assert("bar" not in rdata)

def test_notify():
    # not much to test here...
    r = httpx.post(url+"notify", json={"payload": "merp"})
    assert(r.status_code == 200)
    r = httpx.post(url+"notify", json={"something": "merp"})
    assert(r.status_code == 400)

test_add_subscriber()
test_del_subscriber()
test_list_subscriber()

test_notify()

print("all tests passed")
