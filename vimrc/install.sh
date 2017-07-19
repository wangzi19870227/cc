#!/bin/bash

# back
if [ -f ~/.vim ]; then
    mv ~/.vim ~/.vim.bak
fi

if [ -f ~/.vimrc ]; then
    mv ~/.vimrc ~/.vimrc.bak
fi

# install
cp -r vim ~/.vim
cp vimrc ~/.vimrc
