# Check_In
### 文件说明

各类网站自动签到脚本

### 使用方法

fork本项目后，在Settings->Secrets中新建仓库密码（New repository secret），根据你需要执行的签到脚本进行添加。例如你想对摸鱼派网站进行每日自动签到，则添加name为`MOYUPAI_USERNAME`，value为你摸鱼派登录的账户邮箱或者用户名，另外继续添加name为`MOYUPAI_PASSWORD`，value为你摸鱼派登录的密码，如下图所示

![](https://z3.ax1x.com/2021/10/12/5mKENV.png#shadow)

![](https://z3.ax1x.com/2021/10/12/5mKxV1.png#shadow)

另外，我在Github Actions中默认配置了摸鱼派、掘金两个个网站的签到脚本，虎扑自动登录，但是大家不一定全部都要用，具体来说，你想签到什么网站，修改`.github/workflows/main.yml`文件即可，如下图所示

![](https://z3.ax1x.com/2021/10/13/5uIr2d.png#shadow)


### 参考项目

- [掘金滑动拼图验证码识别](https://github.com/shuai93/juejin)
- [图片验证码ocr](https://github.com/sml2h3/ddddocr)
