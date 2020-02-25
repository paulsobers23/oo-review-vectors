class Vec{
  constructor(x,y){
    this.x = x
    this.y = y
  }
  plus(vec){
    return new Vec(this.x + vec.x, this.y + vec.y)
  }
  minus(vec){
    return new Vec(this.x - vec.x, this.y - vec.y)
  }
  get length(){
    return Math.sqrt(this.x**2 + this.y**2)
  }
  static distance(point1,point2){
    let dx = point2[0] - point1[0]
    let dy = point2[1] - point1[1]
    return Math.sqrt(dx ** 2 + dy ** 2)
  }
}

