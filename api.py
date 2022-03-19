from flask import Flask
import yaml

app = Flask(__name__)

@app.route("//viewall[liberia:1234]")
def all():
    global load
    with open('db.yaml') as f:
        load = yaml.load(f, Loader=yaml.FullLoader)

    return str(load)

@app.route("//view[liberia:1234]/uuid[<UUID>]")
def get(UUID):
    global load
    with open('db.yaml') as f:
        load = yaml.load(f, Loader=yaml.FullLoader)

    return load[UUID]

@app.route("//update[liberia:1234]/uuid[<UUID>]/data[<DATA>]/status[<STATUS>]")
def update(UUID, DATA, STATUS):
    global load
    with open('db.yaml') as f:
        load = yaml.load(f, Loader=yaml.FullLoader)
    if UUID in str(load):
        del load[UUID]
        with open('db.yaml', 'w') as f:
            yaml.dump(load, f)
        with open('db.yaml', 'a') as f:
            f.write(UUID + ":" + "\n")
            f.write(f"  data: {DATA}" + "\n")
            f.write(f"  status: {STATUS}" + "\n")
        return "Success."
    else:
        with open('db.yaml', 'a') as f:
            f.write(UUID + ":" + "\n")
            f.write(f"  data: {DATA}" + "\n")
            f.write(f"  status: {STATUS}" + "\n")
        return "Success."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="1234")