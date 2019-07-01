					; Setup package
(require 'package)

					; No startup package
(setq package-enable-at-startup nil)

					; Set package sources
(setq package-archives '(("melpa" . "https://melpa.org/packages/")
                         ;;("marmalade" . "http://marmalade-repo.org/packages/")
			 ("ELPA"  . "http://tromey.com/elpa/")
			 ("gnu"   . "http://elpa.gnu.org/packages/")
                         ("org" . "https://orgmode.org/elpa/")))

					; Initialize package
(package-initialize)

					; Bootstrap use-package
(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

					; Emacs variables
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-enabled-themes (quote (manoj-dark)))
 '(gnus-undo-limit 20000)
 '(org-agenda-files
   (quote
    ("~/org/todo.org" "~/org/main.org" "~/org/notes.org")))
 '(org-agenda-text-search-extra-files (quote (agenda-archives)))
 '(org-confirm-babel-evaluate nil)
 '(org-cycle-separator-lines 2)
 '(org-default-notes-file "/home/zanzes/org/notes.org")
 '(org-ellipsis " »")
 '(org-enforce-todo-checkbox-dependencies t)
 '(org-enforce-todo-dependencies t)
 '(org-from-is-user-regexp nil)
 '(org-goto-max-level 10)
 '(org-hide-block-startup t)
 '(org-log-done (quote time))
 '(org-log-into-drawer t)
 '(org-log-redeadline (quote time))
 '(org-log-refile (quote time))
 '(org-log-reschedule (quote time))
 '(org-modules
   (quote
    (org-bbdb org-bibtex org-docview org-gnus org-habit org-info org-irc org-mhe org-mouse org-rmail org-w3m)))
 '(org-pretty-entities t)
 '(org-refile-allow-creating-parent-nodes (quote confirm))
 '(org-refile-targets (quote ((org-agenda-files :level . 1))))
 '(org-self-insert-cluster-for-undo t)
 '(org-src-tab-acts-natively t)
 '(org-src-window-setup (quote current-window))
 '(org-track-ordered-property-with-tag t)
 '(package-selected-packages
   (quote
    (web-mode arduino-mode true org-gcal flycheck dumb-jump git-gutter magit projectile org-alert elpy material-theme better-defaults format-all org htmlize which-key volume use-package try threes switch-window swiper sudo-ext sudo-edit spacemacs-theme spaceline-all-the-icons smex smartparens slime rainbow-mode rainbow-delimiters python pulseaudio-control pretty-mode popup-kill-ring paren-completer paredit-menu org-bullets mark-multiple jedi ido-vertical-mode hungry-delete highlight-parentheses golden-ratio gited expand-region dmenu dashboard csv-mode company-statistics company-math company-ebdb beacon ace-window)))
 '(powerline-default-separator (quote alternate)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(org-ellipsis ((t (:foreground "dark magenta" :underline nil)))))

                                        ; Load custom config
(org-babel-load-file (expand-file-name "~/.emacs.d/lzconf.org"))
