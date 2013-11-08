if has("win32") || has ('win64')
    let $VIMHOME = $HOME."/vimfiles/"
else
    let $VIMHOME = $HOME."/.vim/"
endif

function! Replace()
    let n = min([20, line("$")])
    keepjumps exe '1,' . n . 's#<+DATE+>#\1' .  strftime('%F %T') . '#e'
    "Decho "debug message " . &ft. expand('%:t')
    keepjumps exe '1,' . n . 's#<+FILE_NAME+>#' .  expand('%:t') . '#e'
    keepjumps exe '1,' . n . 's#<+FILE_NAME_BASE+>#' .  expand('%:t:r') . '#e'
    keepjumps exe '1,' . n . 's#<+FILE_NAME_U+>#' .  toupper(expand('%:t:r')) . '#e'
    "keepjumps exe '1,' . n . 's#<+FILE_NAME+>#' .  expand('%:t') . '#e'
    "call histdel('search', -1)
endfun

" add templates in templates/ using filetype as file name
"au BufNewFile * :silent! exec "call Decho('abc')"
"au BufNewFile * :silent! exec "call Decho('". expand('%:t')  ."')"
"autocmd BufNewFile *.py 0r ~/.vim/skeletons/s.py | call Replace()
"autocmd BufNewFile *.mkd 0r ~/.vim/skeletons/s.mkd
au BufNewFile * :silent! exec ":0r ".$VIMHOME."skeletons/". &ft . ".skeleton" | call Replace()

autocmd BufNewFile *.h 0r ~/.vim/skeletons/h.skeleton | call Replace()


" If buffer modified, update any 'Last modified: ' in the first 20 lines.
" 'Last modified: ' can have up to 10 characters before (they are retained).
" Restores cursor and window position using save_cursor variable.
function! LastModified()
  if &modified
    let save_cursor = getpos(".")
    let n = min([20, line("$")])
    keepjumps exe '1,' . n . 's#^\(.\{,10}Last modified: \)\S* \S*#\1' .
          \ strftime('%F %T') . '#e'

    "Decho "debug message " 

    "call histdel('search', -1)
    call setpos('.', save_cursor)
  endif
endfun

autocmd BufWritePre * call LastModified()
"autocmd BufReadPre * call LastModified()
