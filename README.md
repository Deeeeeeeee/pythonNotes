# python 笔记

> 笔记记录在 .py 文件中，clone 执行即可

***

# git 笔记

## 开发流程：

### 创建分支
 - git branch dev
 - git branch feature
 
### 切换分支
 - git checkout dev
 
### 添加修改进暂存区
 - git add [filename]
 
### 提交修改
 - git commit -m "change" [filename]
 
### 合并dev分支到本地master(防止分支被误删，还是保持master的更新)
 - git checkout master
 - git merge dev
 
### 推送分支到远程库
 - git push origin dev
 
### 发起pull request，审核后merge到远程库的master分支

### 抓取更新后的远程库的master分支到本地feature分支
 - git checkout feature 
 - git fetch origin master
 - git log -p dev feature
 
> 比较刚抓取的更新和当前dev开发分支有和异同，审核后再合并到dev
 - git checkout dev
 - git merge feature