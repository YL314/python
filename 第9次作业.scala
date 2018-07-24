/**
  * Created by ASUS on 2018/7/20.
  */
object tianqi {
  def main (args:Array[String]): Unit ={
    var temp=List[Int](30,32,35,34,35,30,37)
    println("一周天气气温如下："+temp)
    for (i<-Range(1,7)if (i==3)){
      println("周三气温："+temp(i-1))

    }
}

}
