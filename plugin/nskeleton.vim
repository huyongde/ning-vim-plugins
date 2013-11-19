if !has('python')
    echo "Error: Required vim 73 compiled with +python"
    finish
endif

if !exists('s:nskeleton_did_init')
    let s:script_path = substitute(expand("<sfile>:p"),'\','/','g')
    let s:script_dir = substitute(expand("<sfile>:p:h"),'\','/','g')
    let s:py_dir = s:script_dir.'/../py'

python << EOF
import sys, vim
if not vim.eval("s:py_dir") in sys.path: sys.path.append(vim.eval("s:py_dir"))
import nskeleton
EOF

    let s:nskeleton_did_init= 1
endif

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

autocmd BufNewFile * call LoadSkeleton()


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
