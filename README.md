
# Table of Contents
 <p><div class="lev1 toc-item"><a href="#python-笔记" data-toc-modified-id="python-笔记-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>python 笔记</a></div><div class="lev1 toc-item"><a href="#git-笔记--开发流程" data-toc-modified-id="git-笔记--开发流程-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>git 笔记--开发流程</a></div><div class="lev2 toc-item"><a href="#创建分支" data-toc-modified-id="创建分支-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>创建分支</a></div><div class="lev2 toc-item"><a href="#切换分支" data-toc-modified-id="切换分支-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>切换分支</a></div><div class="lev2 toc-item"><a href="#添加修改进暂存区" data-toc-modified-id="添加修改进暂存区-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>添加修改进暂存区</a></div><div class="lev2 toc-item"><a href="#提交修改" data-toc-modified-id="提交修改-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>提交修改</a></div><div class="lev2 toc-item"><a href="#合并dev分支到本地master(防止分支被误删，还是保持master的更新)" data-toc-modified-id="合并dev分支到本地master(防止分支被误删，还是保持master的更新)-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>合并dev分支到本地master(防止分支被误删，还是保持master的更新)</a></div><div class="lev2 toc-item"><a href="#推送分支到远程库" data-toc-modified-id="推送分支到远程库-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>推送分支到远程库</a></div><div class="lev2 toc-item"><a href="#发起pull-request，审核后merge到远程库的master分支" data-toc-modified-id="发起pull-request，审核后merge到远程库的master分支-27"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>发起pull request，审核后merge到远程库的master分支</a></div><div class="lev2 toc-item"><a href="#抓取更新后的远程库的master分支到本地feature分支" data-toc-modified-id="抓取更新后的远程库的master分支到本地feature分支-28"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>抓取更新后的远程库的master分支到本地feature分支</a></div><div class="lev1 toc-item"><a href="#关于Anaconda" data-toc-modified-id="关于Anaconda-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>关于Anaconda</a></div><div class="lev2 toc-item"><a href="#Anaconda简介" data-toc-modified-id="Anaconda简介-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Anaconda简介</a></div><div class="lev2 toc-item"><a href="#安装(Windows)" data-toc-modified-id="安装(Windows)-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>安装(Windows)</a></div><div class="lev2 toc-item"><a href="#添加环境变量" data-toc-modified-id="添加环境变量-33"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>添加环境变量</a></div><div class="lev2 toc-item"><a href="#测试" data-toc-modified-id="测试-34"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>测试</a></div><div class="lev1 toc-item"><a href="#关于conda的使用" data-toc-modified-id="关于conda的使用-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>关于conda的使用</a></div><div class="lev2 toc-item"><a href="#conda简介" data-toc-modified-id="conda简介-41"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>conda简介</a></div><div class="lev2 toc-item"><a href="#配置源(非常重要！！！)" data-toc-modified-id="配置源(非常重要！！！)-42"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>配置源(非常重要！！！)</a></div><div class="lev3 toc-item"><a href="#方法1" data-toc-modified-id="方法1-421"><span class="toc-item-num">4.2.1&nbsp;&nbsp;</span>方法1</a></div><div class="lev3 toc-item"><a href="#方法2" data-toc-modified-id="方法2-422"><span class="toc-item-num">4.2.2&nbsp;&nbsp;</span>方法2</a></div><div class="lev3 toc-item"><a href="#方法3" data-toc-modified-id="方法3-423"><span class="toc-item-num">4.2.3&nbsp;&nbsp;</span>方法3</a></div><div class="lev2 toc-item"><a href="#常用命令" data-toc-modified-id="常用命令-43"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>常用命令</a></div><div class="lev3 toc-item"><a href="#conda配置-conda-config" data-toc-modified-id="conda配置-conda-config-431"><span class="toc-item-num">4.3.1&nbsp;&nbsp;</span>conda配置 <code>conda config</code></a></div><div class="lev3 toc-item"><a href="#conda自身管理" data-toc-modified-id="conda自身管理-432"><span class="toc-item-num">4.3.2&nbsp;&nbsp;</span>conda自身管理</a></div><div class="lev3 toc-item"><a href="#python环境&amp;多版本python管理" data-toc-modified-id="python环境&amp;多版本python管理-433"><span class="toc-item-num">4.3.3&nbsp;&nbsp;</span>python环境&amp;多版本python管理</a></div><div class="lev4 toc-item"><a href="#创建环境(conda-create)" data-toc-modified-id="创建环境(conda-create)-4331"><span class="toc-item-num">4.3.3.1&nbsp;&nbsp;</span>创建环境(conda create)</a></div><div class="lev4 toc-item"><a href="#切换环境(activate/deactivate)" data-toc-modified-id="切换环境(activate/deactivate)-4332"><span class="toc-item-num">4.3.3.2&nbsp;&nbsp;</span>切换环境(activate/deactivate)</a></div><div class="lev4 toc-item"><a href="#列出所有已创建的环境" data-toc-modified-id="列出所有已创建的环境-4333"><span class="toc-item-num">4.3.3.3&nbsp;&nbsp;</span>列出所有已创建的环境</a></div><div class="lev4 toc-item"><a href="#验证当前环境" data-toc-modified-id="验证当前环境-4334"><span class="toc-item-num">4.3.3.4&nbsp;&nbsp;</span>验证当前环境</a></div><div class="lev4 toc-item"><a href="#克隆一个环境" data-toc-modified-id="克隆一个环境-4335"><span class="toc-item-num">4.3.3.5&nbsp;&nbsp;</span>克隆一个环境</a></div><div class="lev4 toc-item"><a href="#删除一个环境" data-toc-modified-id="删除一个环境-4336"><span class="toc-item-num">4.3.3.6&nbsp;&nbsp;</span>删除一个环境</a></div><div class="lev4 toc-item"><a href="#分享你的环境给其他基友" data-toc-modified-id="分享你的环境给其他基友-4337"><span class="toc-item-num">4.3.3.7&nbsp;&nbsp;</span>分享你的环境给其他基友</a></div><div class="lev3 toc-item"><a href="#conda包管理" data-toc-modified-id="conda包管理-434"><span class="toc-item-num">4.3.4&nbsp;&nbsp;</span>conda包管理</a></div><div class="lev3 toc-item"><a href="#让Anaconda支持R语言" data-toc-modified-id="让Anaconda支持R语言-435"><span class="toc-item-num">4.3.5&nbsp;&nbsp;</span>让Anaconda支持R语言</a></div><div class="lev1 toc-item"><a href="#关于Jupyter" data-toc-modified-id="关于Jupyter-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>关于Jupyter</a></div><div class="lev2 toc-item"><a href="#让Jupyter支持其他语言(R)" data-toc-modified-id="让Jupyter支持其他语言(R)-51"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>让Jupyter支持其他语言(R)</a></div><div class="lev2 toc-item"><a href="#Jupyter命令" data-toc-modified-id="Jupyter命令-52"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Jupyter命令</a></div><div class="lev2 toc-item"><a href="#Jupyter插件" data-toc-modified-id="Jupyter插件-53"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Jupyter插件</a></div>

# python 笔记

笔记记录在```.ipynb```文件中，用**Jupyter**打开。**pychram2017.1**版本开始也支持```.ipynb```文件，也可以用pychram打开

---

# git 笔记--开发流程

## 创建分支

- ```git branch dev```
- ```git branch feature```

## 切换分支

- ```git checkout dev```

## 添加修改进暂存区

- ```git add [filename]```

## 提交修改

- ```git commit -m "change" [filename]```

## 合并dev分支到本地master(防止分支被误删，还是保持master的更新)

 - ```git checkout master```
 - ```git merge dev```

## 推送分支到远程库

- ```git push origin dev```

## 发起pull request，审核后merge到远程库的master分支

## 抓取更新后的远程库的master分支到本地feature分支

- ```git checkout feature```
- ```git fetch origin master```
- ```git log -p dev feature```
>  比较刚抓取的更新和当前dev开发分支有和异同，审核后再合并到dev

- ```git checkout dev```
- ```git merge feature```

---

# 关于Anaconda

## Anaconda简介

[**Anaconda**](https://www.continuum.io/)是一个python**集成环境**，主要面向python科学计算和数据分析上，因此它集成了许多第三方科学计算的库，如 [NumPy](https://docs.scipy.org/doc/numpy/)，[SciPy](https://docs.scipy.org/doc/scipy/reference/)，[matplotlib](http://matplotlib.org/index.html) 等。Anaconda有自己的**包管理**工具[**conda**](https://conda.io/docs/index.html)，类似于**python**的**pip**，但是它的功能用法要强大许多。它有自己的文档，点击前面**conda**链接访问**使用文档**。本文后部分也会介绍**conda**的一些常用命令。

## 安装(Windows)

* 下载[**Anaconda**](https://www.continuum.io/downloads)，如果下不动可以到[这里](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)下载，找自己需要的版本
* 运行安装程序，如 **Anaconda3-4.3.1-Windows-x86_64.exe**，选择要安装的路径，如 **D:\Anaconda3**
* 进行到如下步骤时（如下图），把第一个勾去掉（添加环境变量），我们稍后自己添加。
* 安装
> **如果之前装过python的，建议卸载掉，避免环境变量上的冲突**

## 添加环境变量

* **(右键)计算机(我的电脑)** --> **属性** --> **(左边栏)高级系统设置** --> **(右下)环境变量**
* 在**用户变量**里新建以下三个变量，及其对应值
> - 变量名:**ANACONDA3**  变量值:**(你的安装路径)\Anaconda3** (*如:D:\DevelopTools\Anaconda3*)
  - 变量名:**ANACONDA3_SCRIPTS** 变量值:**(你的安装路径)\Anaconda3\Scripts;(你的安装路径)\Anaconda3\Tools\Scripts** (*如:D:\DevelopTools\Anaconda3\Scripts;D:\DevelopTools\Anaconda3\Tools\Scripts*)
  - 变量名:**ANACONDA3_TOOLS**  变量值:**(你的安装路径)\Anaconda3\Tools** (*如:D:\DevelopTools\Anaconda3\Tools*)

* 在**path**变量名里添加以下三个变量值
> - **%ANACONDA3%**
  - **%ANACONDA3_SCRIPTS%**
  - **%ANACONDA3_TOOLS%**

## 测试

* 打开cmd，输入python，检查版本号与你安装的是否一致。

---

# 关于conda的使用

## conda简介

**conda**是一个开源的**包管理**系统和**环境管理**系统，它专门用来处理安装**多版本**的软件包和依赖，并且能轻松地在之间切换而互不影响。它支持**OSX**，**Linux**，和**Windows**，最初它是为python打包和发布软件专门设计的，现在它支持的语言已经有多种：**Python，R，Ruby，Lua，Scala，Java，Javascript，C/C++，FORTRAN**
> [**官方介绍**](https://conda.io/docs/index.html)
>
**Package, dependency and environment management for any language: Python, R, Ruby, Lua, Scala, Java, Javascript, C/ C++, FORTRAN**
>
Conda is an open source package management system and environment management system for installing multiple versions of software packages and their dependencies and switching easily between them. It works on Linux, OS X and Windows, and was created for Python programs but can package and distribute any software.
>
Conda is included in Anaconda and Miniconda. Conda is also included in the Continuum subscriptions of Anaconda, which provide on-site enterprise package and environment management for Python, R, Node.js, Java, and other application stacks. Conda is also available on pypi, although that approach may not be as up-to-date.
Miniconda is a small “bootstrap” version that includes only conda, Python, and the packages they depend on. Over 720 scientific packages and their dependencies can be installed individually from the Continuum repository with the “conda install” command.
>
Anaconda includes conda, conda-build, Python, and over 150 automatically installed scientific packages and their dependencies. As with Miniconda, over 250 additional scientific packages can be installed individually with the “conda install” command.
>
pip install conda uses the released version on pypi. This version allows you to create new conda environments using any python installation, and a new version of Python will then be installed into those environments. These environments are still considered “Anaconda installations.”
>
The conda command is the primary interface for managing Anaconda installations. It can query and search the Anaconda package index and current Anaconda installation, create new conda environments, and install and update packages into existing conda environments.

## 配置源(非常重要！！！)

conda下载软件包时，默认从**官方源**下载。因为**GFW**的原因，很多时候下载网速会非常慢，甚至访问不到，根本下不下来。这时我们可以通过**更改软件源**来解决这一监介局面。国内比较好的**镜像源站**要数[**清华大学开源软件镜像站**](https://mirrors.tuna.tsinghua.edu.cn/)了，它包含了许多开源镜像，如**LinuxISO**，**Python**，**R**等等。下面我们进行配置

### 方法1

* 找到 **.condarc** 文件，位置在你的**用户目录**下(*如:**C:\Users\username***)
* 用**记事本**或**文本编辑器**打开它
* 把它替换成如下内容:
```
channels:
    - https://pypi.tuna.tsinghua.edu.cn/simple/
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/mro/
show_channel_urls: true
```
> **这几个源基本涵盖了所有需要的软件在里面，包括R语言**

* 保存

### 方法2

* 访问[**Anaconda 镜像使用帮助**](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)，阅读并执行。下面是搬运
* 在终端运行以下命令：
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/mro/
conda config --set show_channel_urls yes
```
> **这几个源基本涵盖了所有需要的软件在里面，包括R语言**

* 找到 **.condarc** 文件，位置在你的用户目录下(*如:**C:\Users\username***)
* 用**记事本**或**文本编辑器**打开它
* 删除 **-default** 一栏

### 方法3

* 打开**PyCharm**
* 选择 **File** --> **Default Settings** --> **Project Interpreter**
* 在**Project Interpreter**下拉栏里选择**Anaconda**的选项
> 如果没有，则点击右边的 **设置** --> **Add Local**，找到**Anaconda**文件夹下的**python.exe**，选中，点击**OK**

* 点击右边的 **+**，弹出 **Available Packages** 窗口，点击下方的 **Manage Repositories**
* 在 **Manage Repositories** 窗口里，点击右边的 **+**，输入以下源链接，**注意，要一条条添加**
```
https://pypi.tuna.tsinghua.edu.cn/simple/
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/
https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/mro/
```

* 删除 **default** 一栏

## 常用命令
**conda** 的官方文档在[这里](https://conda.io/docs/index.html)

### conda配置 ```conda config```

- **conda**的配置信息一般都写在 **.condarc** 文件里，输入 ```conda config --help``` 查看命令参数与用法
> 例：
>
输入：```conda config --show```
>
返回：
```
add_anaconda_token: True
add_pip_as_python_dependency: True
allow_non_channel_urls: True
allow_softlinks: True
always_copy: False
always_softlink: False
always_yes: False
anaconda_upload: None
auto_update_conda: True
changeps1: True
channel_alias: https://conda.anaconda.org
channel_priority: True
channels:
  - https://pypi.tuna.tsinghua.edu.cn/simple/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/mro/
client_ssl_cert:
client_ssl_cert_key:
clobber: False
create_default_packages: []
custom_channels:
  pkgs/free: https://repo.continuum.io/
  pkgs/r: https://repo.continuum.io/
  pkgs/pro: https://repo.continuum.io/
  pkgs/msys2: https://repo.continuum.io/
custom_multichannels:
  defaults: ["https://repo.continuum.io/pkgs/free", "https://repo.continuum.io/pkgs/r", "https://repo.continuum.io/pkgs/pro", "https://repo.continuum.io/pkgs/msys2"]
  local: []
default_channels:
  - https://repo.continuum.io/pkgs/free
  - https://repo.continuum.io/pkgs/r
  - https://repo.continuum.io/pkgs/pro
  - https://repo.continuum.io/pkgs/msys2
disallow: []
envs_dirs:
  - D:\DevelopTools\Anaconda3\envs
  - C:\Users\yang\AppData\Local\conda\conda\envs
  - C:\Users\yang\.conda\envs
force: False
json: False
local_repodata_ttl: 1
migrated_channel_aliases: []
offline: False
path_conflict: clobber
pinned_packages: []
pkgs_dirs:
  - D:\DevelopTools\Anaconda3\pkgs
  - C:\Users\yang\AppData\Local\conda\conda\pkgs
proxy_servers: {}
quiet: False
remote_connect_timeout_secs: 9.15
remote_max_retries: 3
remote_read_timeout_secs: 60.0
rollback_enabled: True
shortcuts: True
show_channel_urls: True
ssl_verify: True
track_features: []
use_pip: True
verbosity: 0
```

### conda自身管理

- 查看conda版本: ```conda --version```
- 升级conda版本: ```conda update conda```

### python环境&多版本python管理
python的版本问题一直以来饱受（我的）诟病，特别是 **python2** 和 **python3** 的语法可是有很大区别，以致于一些库的使用都造成了很大麻烦。但是，你又不希望自己的系统同时装两个，甚至好几个版本的python，光是想怎样切换都是一件头疼的问题。在没有conda之前，我有尝试过 **[virtualenv](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000)** 和 **[pyenv](http://seisman.info/python-pyenv.html)** 这两种python多版本环境管理工具，但是总感觉不太友好。直到我TM遇到了conda...

因为Anaconda是一个面向于**科学计算**的python集成环境，所以它包含的库大多都是做科学计算的。但是像**Web**开发方面的库和框架（如**[Django](https://www.djangoproject.com/)**）Anaconda就没有集成在里面。假如我现在要**用python做Web开发**，而且我**只安装了Anaconda**，我又**不想直接把Django装到Anaconda里面，我想把它跟其他包隔离开来，Anaconda专门处理数据分析的问题**。这时**conda的环境管理**就派上用场了。
> - **输入```conda env --help```查看有关conda环境管理的命令与帮助**

#### 创建环境(conda create)
conda的环境创建一般在**Anaconda\env\\**目录下，假如需要更改路径，输入```conda create --help```查看有关说明

- 假如你的Anaconda版本为python3，现在你想创建一个新的环境，基于python2版本，不含任何第三方库，只是完整干净的python2环境。你只需在终端输入：

```
conda create --name py2 python=2
```
> 这里**py2**是环境名，是自定义的。

- 假如你要创建一个新的环境，用于Web开发，版本与当前Anaconda的python版本一致，需同时包含Django库，你只需在终端输入：

```
conda create --name [这里填你的环境名] django
```

#### 切换环境(activate/deactivate)

- 输入```activate [你的环境名]```激活环境
- 输入```deactivate [你的环境名]```注销环境

#### 列出所有已创建的环境

- 输入```conda info --envs```
- 或者输入```conda env list```

#### 验证当前环境

- 输入```conda info --envs```

#### 克隆一个环境

- 新建环境时，克隆一个已有环境到其中，输入
```conda cerate --name [新环境名] --clone [已有环境名]```

#### 删除一个环境

- 当你想删除某个环境时，输入```conda remove --name [你的环境名]```

#### 分享你的环境给其他基友
你可能会想把你**打包的环境发给你的基友**，这样他就可以轻松的**跑你**(手动滑稽)在这个环境上写的程序，做的有趣的项目。把一切你用到的包，版本和环境打包给他，你只需给他一份**environment.yml**文件的copy

- 首先，激活你想要打包的环境，如**heiheihei**(环境名)，输入```activate heiheihei```
> 注意，假如你已有**environment.yml**文件，那么将会被新文件覆盖

- 导出**environment.yml**文件 ```conda env export > environment.yml```
- 把文件**发(cha)给(ru)**你的基友
- 你的基友根据文件来创建环境 ```conda env create -f environment.yml```
- 基友激活你的的环境**heiheihei** ```activate heiheihei```

**[更多有关环境管理的命令请访问conda官方文档](https://conda.io/docs/using/envs.html)**

### conda包管理

- 查看当前环境已安装的包 ```conda list```
- 查找包，确定是否能安装 ```conda search [包名]```
- 在当前环境安装软件包 ```conda install [包名]```
- 在某一环境安装软件包 ```conda install --name [环境名] [包名]```
- 升级软件包 ```conda update [包名]```，升级conda ```conda update conda```，升级python版本 ```conda update python```
- 删除当前环境软件包 ```conda remove [包名]```
- 删除某一环境软件包 ```conda remove --name [环境名] [包名]```

### 让Anaconda支持R语言
R语言是一个专门用来做统计分析的语言，内置庞大统计分析函数库，为数据分析量身而制。详细介绍访问[R官方网站](https://www.r-project.org/)，这里不在赘述

- 安装所有R语言的包和依赖 ```conda install r r-essentials```
- 升级安装的R包和依赖 ```conda update r r-essentials```

---

# 关于Jupyter

Anaconda里除了一大堆第三方包，还有一些非常**niuchalable**的工具，其中**Jupyter**就是这其中一个。

[**Jupyter**](http://jupyter.org/)全称应该叫**Jupyter Notebook**，顾名思义，Jupyter定义为笔记本。而且Jupyter的确是一种**交互式笔记本**，可以支持**python**在内的多达**40**种语言的输入输出。它的前身（应该是前身）就是出名的 **IPython Notebook**，后来整个Ipython项目升级为Jupyter，就有了现在的Jupyter Notebook

Jupyter Notebook 的本质是一个 **Web 应用程序**，便于创建和共享**文学化程序文档**，支持**实时代码**，**数学方程**，**可视化**和 **markdown**。 用途包括：**数据清理和转换，数值模拟，统计建模，机器学习**等等

Jupyter的使用其实非常容易上手。只要你习惯了这种输入输出方式，你就会觉得写代码和写博客一样有趣(手动滑稽)。当你开始习惯在上面写代码，记笔记时，你就会开始有**折腾**的心理了。下面讲讲我的**折腾（用法）**

> 注意：Jupyter的**输入输出栏（姑且先这么叫）**在Jupyter里称为**cell**。下面有讲到输入输出栏的地方都称作**cell**。

## 让Jupyter支持其他语言(R)

这是我第一个想到要去折腾的事情。因为毕业设计的原因，我需要**微微地**用一下**R语言**做一些统计分析的工作（**微小的工作**）。我那时并没有了解到**Anaconda就可以帮我完成这件工作，只需要一条命令**。我天真地下载了R的安装包，然后查了一堆关键词为 **Jupyter，R** 的资料，经过一轮番配置，才艰难完成。等对conda有一定了解的时候，才知道自己真的**上台拿衣服**。下面说一下Anaconda是如何做到的。

- 首先，完。（其实这一步在**配置源**的时候就已经完成了。就是**添加R的镜像源**，url为以下）

```
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/
https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
```

- 然后，完。（第二步也就是执行**让Anaconda支持R语言**一节里的命令 ```conda install r r-essentials```）
- 最后，打开Jupyter，在**new**下拉菜单里你就会看到**R**这一选项了。

是不是很简单？你以为完了吗？**拿衣服！**所以说有时候**长者**的话，要听完，不然下场就是**上台拿衣服**。

当你在**new**菜单里选择了**R**时，会新建一个**R语言的notebook**。但是你会看到浏览器**蹦出了两个提醒窗口（反正我是看到了）**，具体内容是有关**R**的一个名为**formatR**的**package缺失**的问题。我之前一直都忽略它，因为我发现我依然能正常地在Jupyter里写R代码。但是作为一个**强迫自己成为强迫症患者患者**，绝不容许这种弹窗的出现！！！所以我查了下formatR这个东西，我发现了[这里](https://yihui.name/formatr/)。原来formatR是一个**R语言的自动排版的依赖库**，能进行**排版缩进，语法高亮**的处理。怪不得之前写R的时候总觉得怎么R这么单调，连关键字都没高亮。现在完事大吉。下面是解决过程。你也可以参考[我发现的那个链接](https://yihui.name/formatr/)自己解决。

- 打开Jupyter，新建R notebook
- 在cell里输入 ```install.packages("formatR", repos = "http://cran.rstudio.com")```
- 按 ```shift``` + ```Enter``` 执行

现在，你可以愉快地学习R语言了（手动滑稽）。

## Jupyter命令

这也是我折腾的一个点。写代码，或者说打字吧，最烦就是整天要鼠标键盘来回切。命令的熟悉是必须的。下面讲讲我常用的命令。

首先查看**命令捷键**在**导航栏**的 **Help** --> **Keyboard Shortcuts**选项里

- **命令模式**（按```Esc```），一般在命令模式下才能执行下面的快捷键命令

> 
- ```Enter```：进入**编辑模式**，在当前的cell继续编辑
- ```M```：当前cell变为markdown格式
- ```Y```：当前cell变为代码模式

- **编辑模式**（按```Enter```），一般在命令模式下才能执行下面的快捷键命令

> 
- ```ctrl``` + ```s```：保存
- ```ctrl``` + ```z```：撤销

更多命令请自行探索。

## Jupyter插件

插件是每个软件最有可玩性的地方之一，儿Jupyter作为一个Web应用程序，当然不会缺插件与开发者。不得不说，Jupyter的插件还是挺实用的。

> **一个屌的软件背后通常都会有一堆屌的插件   ----沃·兹基硕德**

要给Jupyter装插件，你需要装以下两个东西
> 
- [jupyter_contrib_nbextensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions)
- [jupyter_nbextensions_configurator](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator)
>
**这两个东西都是github上的项目，他们的安装教程在README里已经有很清晰的描述，非常简单，也是几条命令的事。建议直接参考。这里不再给出安装步骤。**

下面介绍一些好的插件

- [Table of Contents](https://zhuanlan.zhihu.com/p/24029578?refer=learnML)

> 这是一个给markdown生成目录的插件，写东西很爽(手动滑稽)

目前只有这个插件用得比较多，值得推荐。当然还有很多不错的插件如python自动排版插件**Autopep8**，可以根据你需要处理的问题，自动在cell头添加import...的**Snippets Menu**。等等。等待你的发掘
