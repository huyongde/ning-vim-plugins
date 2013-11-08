if !has('python')
    echo "Error: Required vim 73 compiled with +python"
    finish
endif

if !exists('s:keyword_check_did_init')
    let s:script_path = substitute(expand("<sfile>:p"),'\','/','g')
    let s:script_dir = substitute(expand("<sfile>:p:h"),'\','/','g')
    let s:py_dir = s:script_dir.'/../py'

python << EOF
import sys, vim
if not vim.eval("s:py_dir") in sys.path: sys.path.append(vim.eval("s:py_dir"))
import keyword_check
EOF

    let s:keyword_check_did_init= 1
endif

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


autocmd BufWritePre *.rst call KeywordCheck()
"noremap <silent>  <C-S-c> :call format_section_title()<CR>
" auto ChangeToThis
"noremap <C-S-c> :call KeywordCheck()<CR>
