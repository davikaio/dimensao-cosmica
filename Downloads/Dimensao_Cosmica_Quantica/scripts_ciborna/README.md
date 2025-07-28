# 🧠 Ciborna v1.0 · Plataforma Modular de Inteligência Financeira

> Desenvolvido por: **Comandante Wiliam · Ciborna Systems 🛸**

## 🚀 Como rodar os testes
```bash
python bootstrap_tests.py
```

Relatórios gerados automaticamente em `/logs/`

## 📦 Instalar dependências
```bash
pip install -r requirements.txt
```

## 📁 Estrutura do Projeto (atual)

```
├── Dimensao_Cosmica_Quantica/
│   ├── README.md
│   ├── scripts/
│   │   ├── rede_neural.py
│   ├── tests/
│   │   ├── run_all_tests.py
│   │   ├── simulador_execucao_estrategia.py
│   │   ├── simulador_previsao_vazia.py
│   │   ├── test_colunas_desalinhadas.py
│   │   ├── test_dataframe_erro_len.py
│   │   ├── test_dataframe_ok.py
│   │   ├── teste_grafico_plotly_fake.py
│   │   ├── verifica_dataframe_integridade.py
│   ├── utils/
│   │   ├── diagnostico_dataset.py
│   │   ├── log_neural.py
│   │   ├── manipulador_arquivos.py
│   │   ├── normalizador_dados.py
│   │   ├── validador_dados.py
│   │   ├── validador_tipos.py
│   ├── utils_demo.py
├── GitHub - cgohlke_talib-build_ Crie rodas TA-Lib para Windows..html
├── GitHub - cgohlke_talib-build_ Crie rodas TA-Lib para Windows._files/
│   ├── 483428
│   ├── Releases · cgohlke_talib-build_files/
│   │   ├── 483428
│   │   ├── app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-d0d0a6-a7da4270c5f4.js.baixados
│   │   ├── app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-567e0f340e27.js.baixados
│   │   ├── app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-900dde-f953ddf42948.js.baixados
│   │   ├── app_assets_modules_github_ref-selector_ts-7fadf2b0ae65.js.baixados
│   │   ├── app_assets_modules_github_sticky-scroll-into-view_ts-e45aabc67d13.js.baixados
│   │   ├── appearance-settings-631c3b2ed371.js.baixados
│   │   ├── appearance-settings.4e1ca273f504ba849f8c.module.css
│   │   ├── behaviors-b28a404c57f9.js.baixados
│   │   ├── code-5aa9e25e0a2c.css
│   │   ├── code-menu-1c74865ebca2.js.baixados
│   │   ├── codespaces-beb77f9a88fd.js.baixados
│   │   ├── copilot-coding-agent-status-8664d1d4714c.js.baixados
│   │   ├── copilot-coding-agent-status.32796c3e0ecdbdaa8ce6.module.css
│   │   ├── dark-89751e879f8b.css
│   │   ├── dark_high_contrast-67c7180a598a.css
│   │   ├── element-registry-9122ebebdfa4.js.baixados
│   │   ├── environment-89128d48c6ff.js.baixados
│   │   ├── github-58ac3ad6cb3f.css
│   │   ├── github-elements-61d697359136.js.baixados
│   │   ├── global-d0507817f2fa.css
│   │   ├── high-contrast-cookie-a58297b2ebf8.js.baixados
│   │   ├── keyboard-shortcuts-dialog-b3dd4b1cb532.js.baixados
│   │   ├── keyboard-shortcuts-dialog.47de85e2c17af43cefd5.module.css
│   │   ├── light-c59dc71e3a4c.css
│   │   ├── light_high_contrast-4bf0cb726930.css
│   │   ├── notifications-global-eadae94940d6.js.baixados
│   │   ├── notifications-subscriptions-menu-c9ab807bd021.js.baixados
│   │   ├── notifications-subscriptions-menu.07dab7f319b881c93ef5.module.css
│   │   ├── octicons-react-9fd6ca6872cc.js.baixados
│   │   ├── primer-b4bd0459f984.css
│   │   ├── primer-primitives-225433424a87.css
│   │   ├── primer-react-a57080a0a6e8.js.baixados
│   │   ├── primer-react.56caf1a9ff4a5de8a71f.module.css
│   │   ├── react-core-442d3988d6da.js.baixados
│   │   ├── react-lib-8705026b409a.js.baixados
│   │   ├── releases-d27bae89dc62.css
│   │   ├── repositories-05d32eb33e8d.js.baixados
│   │   ├── repository-fa462f1c51f1.css
│   │   ├── sessions-eed3aa0554dd.js.baixados
│   │   ├── ui_packages_agent-sessions_utils_elapsed-time-util_ts-ui_packages_agent-sessions_hooks_useSes-bd1a31-8e88721bfb45.js.baixados
│   │   ├── ui_packages_code-view-shared_components_files-search_FileResultsList_tsx.b824b197dc91fa971d59.module.css
│   │   ├── ui_packages_document-metadata_document-metadata_ts-ui_packages_promise-with-resolvers-polyfil-1e7a2a-b50af437b812.js.baixados
│   │   ├── ui_packages_failbot_failbot_ts-b714866088c2.js.baixados
│   │   ├── ui_packages_ui-commands_ui-commands_ts-b755d908e0b1.js.baixados
│   │   ├── ui_packages_updatable-content_updatable-content_ts-a5daa16ae903.js.baixados
│   │   ├── vendors-node_modules_braintree_browser-detection_dist_browser-detection_js-node_modules_githu-bb80ec-34c4b68b1dd3.js.baixados
│   │   ├── vendors-node_modules_color-convert_index_js-1a149db8dc99.js.baixados
│   │   ├── vendors-node_modules_cookie_index_js-node_modules_primer_live-region-element_dist_esm_index_j-1ca8f6-89ab81577c38.js.baixados
│   │   ├── vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-ea8eaa-eefe25567449.js.baixados
│   │   ├── vendors-node_modules_emotion_is-prop-valid_dist_emotion-is-prop-valid_esm_js-node_modules_emo-b1c483-b5947865157f.js.baixados
│   │   ├── vendors-node_modules_fzy_js_index_js-node_modules_github_paste-markdown_dist_index_js-63a26702fa42.js.baixados
│   │   ├── vendors-node_modules_github_auto-complete-element_dist_index_js-node_modules_github_catalyst_-8e9f78-c1e2fb329866.js.baixados
│   │   ├── vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_remote--3c9c82-aa5ff674466d.js.baixados
│   │   ├── vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-cadbad-fad3eaf3c7ec.js.baixados
│   │   ├── vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-3eebbd-c8d976843cc9.js.baixados
│   │   ├── vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-d8c643-251bc3964eb6.js.baixados
│   │   ├── vendors-node_modules_github_markdown-toolbar-element_dist_index_js-6a8c7d9a08fe.js.baixados
│   │   ├── vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_delegated-events_di-e161aa-7cb68a617c15.js.baixados
│   │   ├── vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_catalyst_lib_inde-dbbea9-558c1f223d1d.js.baixados
│   │   ├── vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_stacktrace-parser_dist_s-1d3d52-babac9434833.js.baixados
│   │   ├── vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_virtualized-list_es_inde-5cfb7e-03a3356911e6.js.baixados
│   │   ├── vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_session-resume_-c1aa61-91618cb63471.js.baixados
│   │   ├── vendors-node_modules_github_relative-time-element_dist_index_js-5913bc24f35d.js.baixados
│   │   ├── vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-70450e-bd02070d35a3.js.baixados
│   │   ├── vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-893f9f-1bcf38e06f01.js.baixados
│   │   ├── vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-94fd67-99b04cc350b5.js.baixados
│   │   ├── vendors-node_modules_github_selector-observer_dist_index_esm_js-cdf2757bd188.js.baixados
│   │   ├── vendors-node_modules_github_text-expander-element_dist_index_js-e50fb7a5fe8c.js.baixados
│   │   ├── vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-595819d3686f.js.baixados
│   │   ├── vendors-node_modules_lit-html_lit-html_js-b93a87060d31.js.baixados
│   │   ├── vendors-node_modules_morphdom_dist_morphdom-esm_js-300e8e4e0414.js.baixados
│   │   ├── vendors-node_modules_oddbird_popover-polyfill_dist_popover-fn_js-a8c266e5f126.js.baixados
│   │   ├── vendors-node_modules_primer_behaviors_dist_esm_index_mjs-c44edfed7f0d.js.baixados
│   │   ├── vendors-node_modules_tanstack_query-core_build_modern_queryObserver_js-node_modules_tanstack_-defd52-0024bc0658ed.js.baixados
│   │   ├── wp-runtime-fe2e65d14445.js.baixados
│   ├── app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-d0d0a6-a7da4270c5f4.js.baixados
│   ├── app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-567e0f340e27.js.baixados
│   ├── app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-900dde-f953ddf42948.js.baixados
│   ├── app_assets_modules_github_ref-selector_ts-7fadf2b0ae65.js.baixados
│   ├── app_assets_modules_github_sticky-scroll-into-view_ts-e45aabc67d13.js.baixados
│   ├── appearance-settings-631c3b2ed371.js.baixados
│   ├── appearance-settings.4e1ca273f504ba849f8c.module.css
│   ├── behaviors-b28a404c57f9.js.baixados
│   ├── code-5aa9e25e0a2c.css
│   ├── code-menu-1c74865ebca2.js.baixados
│   ├── codespaces-beb77f9a88fd.js.baixados
│   ├── copilot-coding-agent-status-8664d1d4714c.js.baixados
│   ├── copilot-coding-agent-status.32796c3e0ecdbdaa8ce6.module.css
│   ├── dark-89751e879f8b.css
│   ├── dark_high_contrast-67c7180a598a.css
│   ├── element-registry-9122ebebdfa4.js.baixados
│   ├── environment-89128d48c6ff.js.baixados
│   ├── github-58ac3ad6cb3f.css
│   ├── github-elements-61d697359136.js.baixados
│   ├── global-d0507817f2fa.css
│   ├── high-contrast-cookie-a58297b2ebf8.js.baixados
│   ├── keyboard-shortcuts-dialog-b3dd4b1cb532.js.baixados
│   ├── keyboard-shortcuts-dialog.47de85e2c17af43cefd5.module.css
│   ├── light-c59dc71e3a4c.css
│   ├── light_high_contrast-4bf0cb726930.css
│   ├── notifications-global-eadae94940d6.js.baixados
│   ├── notifications-subscriptions-menu-c9ab807bd021.js.baixados
│   ├── notifications-subscriptions-menu.07dab7f319b881c93ef5.module.css
│   ├── octicons-react-9fd6ca6872cc.js.baixados
│   ├── primer-b4bd0459f984.css
│   ├── primer-primitives-225433424a87.css
│   ├── primer-react-a57080a0a6e8.js.baixados
│   ├── primer-react.56caf1a9ff4a5de8a71f.module.css
│   ├── react-core-442d3988d6da.js.baixados
│   ├── react-lib-8705026b409a.js.baixados
│   ├── repos-overview-77412ce2acf4.js.baixados
│   ├── repos-overview.884af41a9a66c5d7f845.module.css
│   ├── repositories-05d32eb33e8d.js.baixados
│   ├── repository-fa462f1c51f1.css
│   ├── sessions-eed3aa0554dd.js.baixados
│   ├── ui_packages_agent-sessions_utils_elapsed-time-util_ts-ui_packages_agent-sessions_hooks_useSes-bd1a31-c3680b46734b.js.baixados
│   ├── ui_packages_code-view-shared_components_files-search_FileResultsList_tsx.b824b197dc91fa971d59.module.css
│   ├── ui_packages_code-view-shared_hooks_use-canonical-object_ts-ui_packages_code-view-shared_hooks-6097ef-062d8d9cda55.js.baixados
│   ├── ui_packages_commit-attribution_index_ts-ui_packages_commit-checks-status_index_ts-ui_packages-762eaa-7383c64c0bfd.js.baixados
│   ├── ui_packages_document-metadata_document-metadata_ts-ui_packages_history_history_ts-ui_packages-417c81-00e1a3522739.js.baixados
│   ├── ui_packages_document-metadata_document-metadata_ts-ui_packages_promise-with-resolvers-polyfil-1e7a2a-b50af437b812.js.baixados
│   ├── ui_packages_failbot_failbot_ts-b714866088c2.js.baixados
│   ├── ui_packages_paths_index_ts-63dc0a08b460.js.baixados
│   ├── ui_packages_ref-selector_RefSelector_tsx-d5cdb50eb045.js.baixados
│   ├── ui_packages_ui-commands_ui-commands_ts-b755d908e0b1.js.baixados
│   ├── ui_packages_updatable-content_updatable-content_ts-a5daa16ae903.js.baixados
│   ├── vendors-node_modules_braintree_browser-detection_dist_browser-detection_js-node_modules_githu-bb80ec-34c4b68b1dd3.js.baixados
│   ├── vendors-node_modules_color-convert_index_js-1a149db8dc99.js.baixados
│   ├── vendors-node_modules_cookie_index_js-node_modules_primer_live-region-element_dist_esm_index_j-1ca8f6-89ab81577c38.js.baixados
│   ├── vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-ea8eaa-eefe25567449.js.baixados
│   ├── vendors-node_modules_dompurify_dist_purify_es_mjs-7457ebdd1a1f.js.baixados
│   ├── vendors-node_modules_emotion_is-prop-valid_dist_emotion-is-prop-valid_esm_js-node_modules_emo-b1c483-b5947865157f.js.baixados
│   ├── vendors-node_modules_fzy_js_index_js-node_modules_github_paste-markdown_dist_index_js-63a26702fa42.js.baixados
│   ├── vendors-node_modules_github_auto-complete-element_dist_index_js-node_modules_github_catalyst_-8e9f78-c1e2fb329866.js.baixados
│   ├── vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-189aa3-aa0d1c491a18.js.baixados
│   ├── vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_remote--3c9c82-aa5ff674466d.js.baixados
│   ├── vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-cadbad-fad3eaf3c7ec.js.baixados
│   ├── vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-3eebbd-c8d976843cc9.js.baixados
│   ├── vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-d8c643-251bc3964eb6.js.baixados
│   ├── vendors-node_modules_github_markdown-toolbar-element_dist_index_js-6a8c7d9a08fe.js.baixados
│   ├── vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_delegated-events_di-e161aa-7cb68a617c15.js.baixados
│   ├── vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_catalyst_lib_inde-dbbea9-558c1f223d1d.js.baixados
│   ├── vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_stacktrace-parser_dist_s-1d3d52-babac9434833.js.baixados
│   ├── vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_virtualized-list_es_inde-5cfb7e-03a3356911e6.js.baixados
│   ├── vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_session-resume_-c1aa61-91618cb63471.js.baixados
│   ├── vendors-node_modules_github_relative-time-element_dist_index_js-5913bc24f35d.js.baixados
│   ├── vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-70450e-bd02070d35a3.js.baixados
│   ├── vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-893f9f-1bcf38e06f01.js.baixados
│   ├── vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-94fd67-99b04cc350b5.js.baixados
│   ├── vendors-node_modules_github_selector-observer_dist_index_esm_js-cdf2757bd188.js.baixados
│   ├── vendors-node_modules_github_text-expander-element_dist_index_js-e50fb7a5fe8c.js.baixados
│   ├── vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-595819d3686f.js.baixados
│   ├── vendors-node_modules_lit-html_lit-html_js-b93a87060d31.js.baixados
│   ├── vendors-node_modules_morphdom_dist_morphdom-esm_js-300e8e4e0414.js.baixados
│   ├── vendors-node_modules_oddbird_popover-polyfill_dist_popover-fn_js-a8c266e5f126.js.baixados
│   ├── vendors-node_modules_primer_behaviors_dist_esm_index_mjs-c44edfed7f0d.js.baixados
│   ├── vendors-node_modules_tanstack_query-core_build_modern_queryObserver_js-node_modules_tanstack_-defd52-0024bc0658ed.js.baixados
│   ├── vendors-node_modules_tanstack_react-virtual_dist_esm_index_js-807aab04afeb.js.baixados
│   ├── wp-runtime-fe2e65d14445.js.baixados
├── README.md
├── Rodar_Ciborna.bat
├── SALVAMENTO DE IA,MEMORI MENTE DE IA PI!!.txt
├── ciborna.png
├── ciborna_env2/
│   ├── Include/
│   ├── Lib/
│   │   ├── site-packages/
│   │   │   ├── _distutils_hack/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── override.py
│   │   │   ├── distutils-precedence.pth
│   │   │   ├── pip/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── __main__.py
│   │   │   │   ├── __pip-runner__.py
│   │   │   │   ├── _internal/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── build_env.py
│   │   │   │   │   ├── cache.py
│   │   │   │   │   ├── cli/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── autocompletion.py
│   │   │   │   │   │   ├── base_command.py
│   │   │   │   │   │   ├── cmdoptions.py
│   │   │   │   │   │   ├── command_context.py
│   │   │   │   │   │   ├── main.py
│   │   │   │   │   │   ├── main_parser.py
│   │   │   │   │   │   ├── parser.py
│   │   │   │   │   │   ├── progress_bars.py
│   │   │   │   │   │   ├── req_command.py
│   │   │   │   │   │   ├── spinners.py
│   │   │   │   │   │   ├── status_codes.py
│   │   │   │   │   ├── commands/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── cache.py
│   │   │   │   │   │   ├── check.py
│   │   │   │   │   │   ├── completion.py
│   │   │   │   │   │   ├── configuration.py
│   │   │   │   │   │   ├── debug.py
│   │   │   │   │   │   ├── download.py
│   │   │   │   │   │   ├── freeze.py
│   │   │   │   │   │   ├── hash.py
│   │   │   │   │   │   ├── help.py
│   │   │   │   │   │   ├── index.py
│   │   │   │   │   │   ├── inspect.py
│   │   │   │   │   │   ├── install.py
│   │   │   │   │   │   ├── list.py
│   │   │   │   │   │   ├── search.py
│   │   │   │   │   │   ├── show.py
│   │   │   │   │   │   ├── uninstall.py
│   │   │   │   │   │   ├── wheel.py
│   │   │   │   │   ├── configuration.py
│   │   │   │   │   ├── distributions/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── base.py
│   │   │   │   │   │   ├── installed.py
│   │   │   │   │   │   ├── sdist.py
│   │   │   │   │   │   ├── wheel.py
│   │   │   │   │   ├── exceptions.py
│   │   │   │   │   ├── index/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── collector.py
│   │   │   │   │   │   ├── package_finder.py
│   │   │   │   │   │   ├── sources.py
│   │   │   │   │   ├── locations/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _distutils.py
│   │   │   │   │   │   ├── _sysconfig.py
│   │   │   │   │   │   ├── base.py
│   │   │   │   │   ├── main.py
│   │   │   │   │   ├── metadata/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _json.py
│   │   │   │   │   │   ├── base.py
│   │   │   │   │   │   ├── importlib/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── _compat.py
│   │   │   │   │   │   │   ├── _dists.py
│   │   │   │   │   │   │   ├── _envs.py
│   │   │   │   │   │   ├── pkg_resources.py
│   │   │   │   │   ├── models/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── candidate.py
│   │   │   │   │   │   ├── direct_url.py
│   │   │   │   │   │   ├── format_control.py
│   │   │   │   │   │   ├── index.py
│   │   │   │   │   │   ├── installation_report.py
│   │   │   │   │   │   ├── link.py
│   │   │   │   │   │   ├── scheme.py
│   │   │   │   │   │   ├── search_scope.py
│   │   │   │   │   │   ├── selection_prefs.py
│   │   │   │   │   │   ├── target_python.py
│   │   │   │   │   │   ├── wheel.py
│   │   │   │   │   ├── network/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── auth.py
│   │   │   │   │   │   ├── cache.py
│   │   │   │   │   │   ├── download.py
│   │   │   │   │   │   ├── lazy_wheel.py
│   │   │   │   │   │   ├── session.py
│   │   │   │   │   │   ├── utils.py
│   │   │   │   │   │   ├── xmlrpc.py
│   │   │   │   │   ├── operations/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── build/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── build_tracker.py
│   │   │   │   │   │   │   ├── metadata.py
│   │   │   │   │   │   │   ├── metadata_editable.py
│   │   │   │   │   │   │   ├── metadata_legacy.py
│   │   │   │   │   │   │   ├── wheel.py
│   │   │   │   │   │   │   ├── wheel_editable.py
│   │   │   │   │   │   │   ├── wheel_legacy.py
│   │   │   │   │   │   ├── check.py
│   │   │   │   │   │   ├── freeze.py
│   │   │   │   │   │   ├── install/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── editable_legacy.py
│   │   │   │   │   │   │   ├── wheel.py
│   │   │   │   │   │   ├── prepare.py
│   │   │   │   │   ├── pyproject.py
│   │   │   │   │   ├── req/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── constructors.py
│   │   │   │   │   │   ├── req_file.py
│   │   │   │   │   │   ├── req_install.py
│   │   │   │   │   │   ├── req_set.py
│   │   │   │   │   │   ├── req_uninstall.py
│   │   │   │   │   ├── resolution/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── base.py
│   │   │   │   │   │   ├── legacy/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── resolver.py
│   │   │   │   │   │   ├── resolvelib/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── base.py
│   │   │   │   │   │   │   ├── candidates.py
│   │   │   │   │   │   │   ├── factory.py
│   │   │   │   │   │   │   ├── found_candidates.py
│   │   │   │   │   │   │   ├── provider.py
│   │   │   │   │   │   │   ├── reporter.py
│   │   │   │   │   │   │   ├── requirements.py
│   │   │   │   │   │   │   ├── resolver.py
│   │   │   │   │   ├── self_outdated_check.py
│   │   │   │   │   ├── utils/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _jaraco_text.py
│   │   │   │   │   │   ├── _log.py
│   │   │   │   │   │   ├── appdirs.py
│   │   │   │   │   │   ├── compat.py
│   │   │   │   │   │   ├── compatibility_tags.py
│   │   │   │   │   │   ├── datetime.py
│   │   │   │   │   │   ├── deprecation.py
│   │   │   │   │   │   ├── direct_url_helpers.py
│   │   │   │   │   │   ├── egg_link.py
│   │   │   │   │   │   ├── encoding.py
│   │   │   │   │   │   ├── entrypoints.py
│   │   │   │   │   │   ├── filesystem.py
│   │   │   │   │   │   ├── filetypes.py
│   │   │   │   │   │   ├── glibc.py
│   │   │   │   │   │   ├── hashes.py
│   │   │   │   │   │   ├── logging.py
│   │   │   │   │   │   ├── misc.py
│   │   │   │   │   │   ├── models.py
│   │   │   │   │   │   ├── packaging.py
│   │   │   │   │   │   ├── setuptools_build.py
│   │   │   │   │   │   ├── subprocess.py
│   │   │   │   │   │   ├── temp_dir.py
│   │   │   │   │   │   ├── unpacking.py
│   │   │   │   │   │   ├── urls.py
│   │   │   │   │   │   ├── virtualenv.py
│   │   │   │   │   │   ├── wheel.py
│   │   │   │   │   ├── vcs/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── bazaar.py
│   │   │   │   │   │   ├── git.py
│   │   │   │   │   │   ├── mercurial.py
│   │   │   │   │   │   ├── subversion.py
│   │   │   │   │   │   ├── versioncontrol.py
│   │   │   │   │   ├── wheel_builder.py
│   │   │   │   ├── _vendor/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── cachecontrol/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _cmd.py
│   │   │   │   │   │   ├── adapter.py
│   │   │   │   │   │   ├── cache.py
│   │   │   │   │   │   ├── caches/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── file_cache.py
│   │   │   │   │   │   │   ├── redis_cache.py
│   │   │   │   │   │   ├── controller.py
│   │   │   │   │   │   ├── filewrapper.py
│   │   │   │   │   │   ├── heuristics.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   │   ├── serialize.py
│   │   │   │   │   │   ├── wrapper.py
│   │   │   │   │   ├── certifi/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __main__.py
│   │   │   │   │   │   ├── cacert.pem
│   │   │   │   │   │   ├── core.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   ├── chardet/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── big5freq.py
│   │   │   │   │   │   ├── big5prober.py
│   │   │   │   │   │   ├── chardistribution.py
│   │   │   │   │   │   ├── charsetgroupprober.py
│   │   │   │   │   │   ├── charsetprober.py
│   │   │   │   │   │   ├── cli/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── chardetect.py
│   │   │   │   │   │   ├── codingstatemachine.py
│   │   │   │   │   │   ├── codingstatemachinedict.py
│   │   │   │   │   │   ├── cp949prober.py
│   │   │   │   │   │   ├── enums.py
│   │   │   │   │   │   ├── escprober.py
│   │   │   │   │   │   ├── escsm.py
│   │   │   │   │   │   ├── eucjpprober.py
│   │   │   │   │   │   ├── euckrfreq.py
│   │   │   │   │   │   ├── euckrprober.py
│   │   │   │   │   │   ├── euctwfreq.py
│   │   │   │   │   │   ├── euctwprober.py
│   │   │   │   │   │   ├── gb2312freq.py
│   │   │   │   │   │   ├── gb2312prober.py
│   │   │   │   │   │   ├── hebrewprober.py
│   │   │   │   │   │   ├── jisfreq.py
│   │   │   │   │   │   ├── johabfreq.py
│   │   │   │   │   │   ├── johabprober.py
│   │   │   │   │   │   ├── jpcntx.py
│   │   │   │   │   │   ├── langbulgarianmodel.py
│   │   │   │   │   │   ├── langgreekmodel.py
│   │   │   │   │   │   ├── langhebrewmodel.py
│   │   │   │   │   │   ├── langhungarianmodel.py
│   │   │   │   │   │   ├── langrussianmodel.py
│   │   │   │   │   │   ├── langthaimodel.py
│   │   │   │   │   │   ├── langturkishmodel.py
│   │   │   │   │   │   ├── latin1prober.py
│   │   │   │   │   │   ├── macromanprober.py
│   │   │   │   │   │   ├── mbcharsetprober.py
│   │   │   │   │   │   ├── mbcsgroupprober.py
│   │   │   │   │   │   ├── mbcssm.py
│   │   │   │   │   │   ├── metadata/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── languages.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   │   ├── resultdict.py
│   │   │   │   │   │   ├── sbcharsetprober.py
│   │   │   │   │   │   ├── sbcsgroupprober.py
│   │   │   │   │   │   ├── sjisprober.py
│   │   │   │   │   │   ├── universaldetector.py
│   │   │   │   │   │   ├── utf1632prober.py
│   │   │   │   │   │   ├── utf8prober.py
│   │   │   │   │   │   ├── version.py
│   │   │   │   │   ├── colorama/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── ansi.py
│   │   │   │   │   │   ├── ansitowin32.py
│   │   │   │   │   │   ├── initialise.py
│   │   │   │   │   │   ├── tests/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── ansi_test.py
│   │   │   │   │   │   │   ├── ansitowin32_test.py
│   │   │   │   │   │   │   ├── initialise_test.py
│   │   │   │   │   │   │   ├── isatty_test.py
│   │   │   │   │   │   │   ├── utils.py
│   │   │   │   │   │   │   ├── winterm_test.py
│   │   │   │   │   │   ├── win32.py
│   │   │   │   │   │   ├── winterm.py
│   │   │   │   │   ├── distlib/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── compat.py
│   │   │   │   │   │   ├── database.py
│   │   │   │   │   │   ├── index.py
│   │   │   │   │   │   ├── locators.py
│   │   │   │   │   │   ├── manifest.py
│   │   │   │   │   │   ├── markers.py
│   │   │   │   │   │   ├── metadata.py
│   │   │   │   │   │   ├── resources.py
│   │   │   │   │   │   ├── scripts.py
│   │   │   │   │   │   ├── t32.exe
│   │   │   │   │   │   ├── t64-arm.exe
│   │   │   │   │   │   ├── t64.exe
│   │   │   │   │   │   ├── util.py
│   │   │   │   │   │   ├── version.py
│   │   │   │   │   │   ├── w32.exe
│   │   │   │   │   │   ├── w64-arm.exe
│   │   │   │   │   │   ├── w64.exe
│   │   │   │   │   │   ├── wheel.py
│   │   │   │   │   ├── distro/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __main__.py
│   │   │   │   │   │   ├── distro.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   ├── idna/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── codec.py
│   │   │   │   │   │   ├── compat.py
│   │   │   │   │   │   ├── core.py
│   │   │   │   │   │   ├── idnadata.py
│   │   │   │   │   │   ├── intranges.py
│   │   │   │   │   │   ├── package_data.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   │   ├── uts46data.py
│   │   │   │   │   ├── msgpack/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── exceptions.py
│   │   │   │   │   │   ├── ext.py
│   │   │   │   │   │   ├── fallback.py
│   │   │   │   │   ├── packaging/
│   │   │   │   │   │   ├── __about__.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _manylinux.py
│   │   │   │   │   │   ├── _musllinux.py
│   │   │   │   │   │   ├── _structures.py
│   │   │   │   │   │   ├── markers.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   │   ├── requirements.py
│   │   │   │   │   │   ├── specifiers.py
│   │   │   │   │   │   ├── tags.py
│   │   │   │   │   │   ├── utils.py
│   │   │   │   │   │   ├── version.py
│   │   │   │   │   ├── pkg_resources/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── platformdirs/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __main__.py
│   │   │   │   │   │   ├── android.py
│   │   │   │   │   │   ├── api.py
│   │   │   │   │   │   ├── macos.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   │   ├── unix.py
│   │   │   │   │   │   ├── version.py
│   │   │   │   │   │   ├── windows.py
│   │   │   │   │   ├── pygments/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __main__.py
│   │   │   │   │   │   ├── cmdline.py
│   │   │   │   │   │   ├── console.py
│   │   │   │   │   │   ├── filter.py
│   │   │   │   │   │   ├── filters/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── formatter.py
│   │   │   │   │   │   ├── formatters/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── _mapping.py
│   │   │   │   │   │   │   ├── bbcode.py
│   │   │   │   │   │   │   ├── groff.py
│   │   │   │   │   │   │   ├── html.py
│   │   │   │   │   │   │   ├── img.py
│   │   │   │   │   │   │   ├── irc.py
│   │   │   │   │   │   │   ├── latex.py
│   │   │   │   │   │   │   ├── other.py
│   │   │   │   │   │   │   ├── pangomarkup.py
│   │   │   │   │   │   │   ├── rtf.py
│   │   │   │   │   │   │   ├── svg.py
│   │   │   │   │   │   │   ├── terminal.py
│   │   │   │   │   │   │   ├── terminal256.py
│   │   │   │   │   │   ├── lexer.py
│   │   │   │   │   │   ├── lexers/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── _mapping.py
│   │   │   │   │   │   │   ├── python.py
│   │   │   │   │   │   ├── modeline.py
│   │   │   │   │   │   ├── plugin.py
│   │   │   │   │   │   ├── regexopt.py
│   │   │   │   │   │   ├── scanner.py
│   │   │   │   │   │   ├── sphinxext.py
│   │   │   │   │   │   ├── style.py
│   │   │   │   │   │   ├── styles/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── token.py
│   │   │   │   │   │   ├── unistring.py
│   │   │   │   │   │   ├── util.py
│   │   │   │   │   ├── pyparsing/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── actions.py
│   │   │   │   │   │   ├── common.py
│   │   │   │   │   │   ├── core.py
│   │   │   │   │   │   ├── diagram/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── exceptions.py
│   │   │   │   │   │   ├── helpers.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   │   ├── results.py
│   │   │   │   │   │   ├── testing.py
│   │   │   │   │   │   ├── unicode.py
│   │   │   │   │   │   ├── util.py
│   │   │   │   │   ├── pyproject_hooks/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _compat.py
│   │   │   │   │   │   ├── _impl.py
│   │   │   │   │   │   ├── _in_process/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── _in_process.py
│   │   │   │   │   ├── requests/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __version__.py
│   │   │   │   │   │   ├── _internal_utils.py
│   │   │   │   │   │   ├── adapters.py
│   │   │   │   │   │   ├── api.py
│   │   │   │   │   │   ├── auth.py
│   │   │   │   │   │   ├── certs.py
│   │   │   │   │   │   ├── compat.py
│   │   │   │   │   │   ├── cookies.py
│   │   │   │   │   │   ├── exceptions.py
│   │   │   │   │   │   ├── help.py
│   │   │   │   │   │   ├── hooks.py
│   │   │   │   │   │   ├── models.py
│   │   │   │   │   │   ├── packages.py
│   │   │   │   │   │   ├── sessions.py
│   │   │   │   │   │   ├── status_codes.py
│   │   │   │   │   │   ├── structures.py
│   │   │   │   │   │   ├── utils.py
│   │   │   │   │   ├── resolvelib/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── compat/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── collections_abc.py
│   │   │   │   │   │   ├── providers.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   │   ├── reporters.py
│   │   │   │   │   │   ├── resolvers.py
│   │   │   │   │   │   ├── structs.py
│   │   │   │   │   ├── rich/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── __main__.py
│   │   │   │   │   │   ├── _cell_widths.py
│   │   │   │   │   │   ├── _emoji_codes.py
│   │   │   │   │   │   ├── _emoji_replace.py
│   │   │   │   │   │   ├── _export_format.py
│   │   │   │   │   │   ├── _extension.py
│   │   │   │   │   │   ├── _fileno.py
│   │   │   │   │   │   ├── _inspect.py
│   │   │   │   │   │   ├── _log_render.py
│   │   │   │   │   │   ├── _loop.py
│   │   │   │   │   │   ├── _null_file.py
│   │   │   │   │   │   ├── _palettes.py
│   │   │   │   │   │   ├── _pick.py
│   │   │   │   │   │   ├── _ratio.py
│   │   │   │   │   │   ├── _spinners.py
│   │   │   │   │   │   ├── _stack.py
│   │   │   │   │   │   ├── _timer.py
│   │   │   │   │   │   ├── _win32_console.py
│   │   │   │   │   │   ├── _windows.py
│   │   │   │   │   │   ├── _windows_renderer.py
│   │   │   │   │   │   ├── _wrap.py
│   │   │   │   │   │   ├── abc.py
│   │   │   │   │   │   ├── align.py
│   │   │   │   │   │   ├── ansi.py
│   │   │   │   │   │   ├── bar.py
│   │   │   │   │   │   ├── box.py
│   │   │   │   │   │   ├── cells.py
│   │   │   │   │   │   ├── color.py
│   │   │   │   │   │   ├── color_triplet.py
│   │   │   │   │   │   ├── columns.py
│   │   │   │   │   │   ├── console.py
│   │   │   │   │   │   ├── constrain.py
│   │   │   │   │   │   ├── containers.py
│   │   │   │   │   │   ├── control.py
│   │   │   │   │   │   ├── default_styles.py
│   │   │   │   │   │   ├── diagnose.py
│   │   │   │   │   │   ├── emoji.py
│   │   │   │   │   │   ├── errors.py
│   │   │   │   │   │   ├── file_proxy.py
│   │   │   │   │   │   ├── filesize.py
│   │   │   │   │   │   ├── highlighter.py
│   │   │   │   │   │   ├── json.py
│   │   │   │   │   │   ├── jupyter.py
│   │   │   │   │   │   ├── layout.py
│   │   │   │   │   │   ├── live.py
│   │   │   │   │   │   ├── live_render.py
│   │   │   │   │   │   ├── logging.py
│   │   │   │   │   │   ├── markup.py
│   │   │   │   │   │   ├── measure.py
│   │   │   │   │   │   ├── padding.py
│   │   │   │   │   │   ├── pager.py
│   │   │   │   │   │   ├── palette.py
│   │   │   │   │   │   ├── panel.py
│   │   │   │   │   │   ├── pretty.py
│   │   │   │   │   │   ├── progress.py
│   │   │   │   │   │   ├── progress_bar.py
│   │   │   │   │   │   ├── prompt.py
│   │   │   │   │   │   ├── protocol.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   │   ├── region.py
│   │   │   │   │   │   ├── repr.py
│   │   │   │   │   │   ├── rule.py
│   │   │   │   │   │   ├── scope.py
│   │   │   │   │   │   ├── screen.py
│   │   │   │   │   │   ├── segment.py
│   │   │   │   │   │   ├── spinner.py
│   │   │   │   │   │   ├── status.py
│   │   │   │   │   │   ├── style.py
│   │   │   │   │   │   ├── styled.py
│   │   │   │   │   │   ├── syntax.py
│   │   │   │   │   │   ├── table.py
│   │   │   │   │   │   ├── terminal_theme.py
│   │   │   │   │   │   ├── text.py
│   │   │   │   │   │   ├── theme.py
│   │   │   │   │   │   ├── themes.py
│   │   │   │   │   │   ├── traceback.py
│   │   │   │   │   │   ├── tree.py
│   │   │   │   │   ├── six.py
│   │   │   │   │   ├── tenacity/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _asyncio.py
│   │   │   │   │   │   ├── _utils.py
│   │   │   │   │   │   ├── after.py
│   │   │   │   │   │   ├── before.py
│   │   │   │   │   │   ├── before_sleep.py
│   │   │   │   │   │   ├── nap.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   │   ├── retry.py
│   │   │   │   │   │   ├── stop.py
│   │   │   │   │   │   ├── tornadoweb.py
│   │   │   │   │   │   ├── wait.py
│   │   │   │   │   ├── tomli/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _parser.py
│   │   │   │   │   │   ├── _re.py
│   │   │   │   │   │   ├── _types.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   ├── truststore/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _api.py
│   │   │   │   │   │   ├── _macos.py
│   │   │   │   │   │   ├── _openssl.py
│   │   │   │   │   │   ├── _ssl_constants.py
│   │   │   │   │   │   ├── _windows.py
│   │   │   │   │   │   ├── py.typed
│   │   │   │   │   ├── typing_extensions.py
│   │   │   │   │   ├── urllib3/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _collections.py
│   │   │   │   │   │   ├── _version.py
│   │   │   │   │   │   ├── connection.py
│   │   │   │   │   │   ├── connectionpool.py
│   │   │   │   │   │   ├── contrib/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── _appengine_environ.py
│   │   │   │   │   │   │   ├── _securetransport/
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── bindings.py
│   │   │   │   │   │   │   │   ├── low_level.py
│   │   │   │   │   │   │   ├── appengine.py
│   │   │   │   │   │   │   ├── ntlmpool.py
│   │   │   │   │   │   │   ├── pyopenssl.py
│   │   │   │   │   │   │   ├── securetransport.py
│   │   │   │   │   │   │   ├── socks.py
│   │   │   │   │   │   ├── exceptions.py
│   │   │   │   │   │   ├── fields.py
│   │   │   │   │   │   ├── filepost.py
│   │   │   │   │   │   ├── packages/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── backports/
│   │   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   │   ├── makefile.py
│   │   │   │   │   │   │   │   ├── weakref_finalize.py
│   │   │   │   │   │   │   ├── six.py
│   │   │   │   │   │   ├── poolmanager.py
│   │   │   │   │   │   ├── request.py
│   │   │   │   │   │   ├── response.py
│   │   │   │   │   │   ├── util/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── connection.py
│   │   │   │   │   │   │   ├── proxy.py
│   │   │   │   │   │   │   ├── queue.py
│   │   │   │   │   │   │   ├── request.py
│   │   │   │   │   │   │   ├── response.py
│   │   │   │   │   │   │   ├── retry.py
│   │   │   │   │   │   │   ├── ssl_.py
│   │   │   │   │   │   │   ├── ssl_match_hostname.py
│   │   │   │   │   │   │   ├── ssltransport.py
│   │   │   │   │   │   │   ├── timeout.py
│   │   │   │   │   │   │   ├── url.py
│   │   │   │   │   │   │   ├── wait.py
│   │   │   │   │   ├── vendor.txt
│   │   │   │   │   ├── webencodings/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── labels.py
│   │   │   │   │   │   ├── mklabels.py
│   │   │   │   │   │   ├── tests.py
│   │   │   │   │   │   ├── x_user_defined.py
│   │   │   │   ├── py.typed
│   │   │   ├── pip-24.0.dist-info/
│   │   │   │   ├── AUTHORS.txt
│   │   │   │   ├── INSTALLER
│   │   │   │   ├── LICENSE.txt
│   │   │   │   ├── METADATA
│   │   │   │   ├── RECORD
│   │   │   │   ├── REQUESTED
│   │   │   │   ├── WHEEL
│   │   │   │   ├── entry_points.txt
│   │   │   │   ├── top_level.txt
│   │   │   ├── pkg_resources/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── _vendor/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── appdirs.py
│   │   │   │   │   ├── importlib_resources/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _adapters.py
│   │   │   │   │   │   ├── _common.py
│   │   │   │   │   │   ├── _compat.py
│   │   │   │   │   │   ├── _itertools.py
│   │   │   │   │   │   ├── _legacy.py
│   │   │   │   │   │   ├── abc.py
│   │   │   │   │   │   ├── readers.py
│   │   │   │   │   │   ├── simple.py
│   │   │   │   │   ├── jaraco/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── context.py
│   │   │   │   │   │   ├── functools.py
│   │   │   │   │   │   ├── text/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── more_itertools/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── more.py
│   │   │   │   │   │   ├── recipes.py
│   │   │   │   │   ├── packaging/
│   │   │   │   │   │   ├── __about__.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _manylinux.py
│   │   │   │   │   │   ├── _musllinux.py
│   │   │   │   │   │   ├── _structures.py
│   │   │   │   │   │   ├── markers.py
│   │   │   │   │   │   ├── requirements.py
│   │   │   │   │   │   ├── specifiers.py
│   │   │   │   │   │   ├── tags.py
│   │   │   │   │   │   ├── utils.py
│   │   │   │   │   │   ├── version.py
│   │   │   │   │   ├── pyparsing/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── actions.py
│   │   │   │   │   │   ├── common.py
│   │   │   │   │   │   ├── core.py
│   │   │   │   │   │   ├── diagram/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── exceptions.py
│   │   │   │   │   │   ├── helpers.py
│   │   │   │   │   │   ├── results.py
│   │   │   │   │   │   ├── testing.py
│   │   │   │   │   │   ├── unicode.py
│   │   │   │   │   │   ├── util.py
│   │   │   │   │   ├── zipp.py
│   │   │   │   ├── extern/
│   │   │   │   │   ├── __init__.py
│   │   │   ├── setuptools/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── _deprecation_warning.py
│   │   │   │   ├── _distutils/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _collections.py
│   │   │   │   │   ├── _functools.py
│   │   │   │   │   ├── _macos_compat.py
│   │   │   │   │   ├── _msvccompiler.py
│   │   │   │   │   ├── archive_util.py
│   │   │   │   │   ├── bcppcompiler.py
│   │   │   │   │   ├── ccompiler.py
│   │   │   │   │   ├── cmd.py
│   │   │   │   │   ├── command/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _framework_compat.py
│   │   │   │   │   │   ├── bdist.py
│   │   │   │   │   │   ├── bdist_dumb.py
│   │   │   │   │   │   ├── bdist_rpm.py
│   │   │   │   │   │   ├── build.py
│   │   │   │   │   │   ├── build_clib.py
│   │   │   │   │   │   ├── build_ext.py
│   │   │   │   │   │   ├── build_py.py
│   │   │   │   │   │   ├── build_scripts.py
│   │   │   │   │   │   ├── check.py
│   │   │   │   │   │   ├── clean.py
│   │   │   │   │   │   ├── config.py
│   │   │   │   │   │   ├── install.py
│   │   │   │   │   │   ├── install_data.py
│   │   │   │   │   │   ├── install_egg_info.py
│   │   │   │   │   │   ├── install_headers.py
│   │   │   │   │   │   ├── install_lib.py
│   │   │   │   │   │   ├── install_scripts.py
│   │   │   │   │   │   ├── py37compat.py
│   │   │   │   │   │   ├── register.py
│   │   │   │   │   │   ├── sdist.py
│   │   │   │   │   │   ├── upload.py
│   │   │   │   │   ├── config.py
│   │   │   │   │   ├── core.py
│   │   │   │   │   ├── cygwinccompiler.py
│   │   │   │   │   ├── debug.py
│   │   │   │   │   ├── dep_util.py
│   │   │   │   │   ├── dir_util.py
│   │   │   │   │   ├── dist.py
│   │   │   │   │   ├── errors.py
│   │   │   │   │   ├── extension.py
│   │   │   │   │   ├── fancy_getopt.py
│   │   │   │   │   ├── file_util.py
│   │   │   │   │   ├── filelist.py
│   │   │   │   │   ├── log.py
│   │   │   │   │   ├── msvc9compiler.py
│   │   │   │   │   ├── msvccompiler.py
│   │   │   │   │   ├── py38compat.py
│   │   │   │   │   ├── py39compat.py
│   │   │   │   │   ├── spawn.py
│   │   │   │   │   ├── sysconfig.py
│   │   │   │   │   ├── text_file.py
│   │   │   │   │   ├── unixccompiler.py
│   │   │   │   │   ├── util.py
│   │   │   │   │   ├── version.py
│   │   │   │   │   ├── versionpredicate.py
│   │   │   │   ├── _entry_points.py
│   │   │   │   ├── _imp.py
│   │   │   │   ├── _importlib.py
│   │   │   │   ├── _itertools.py
│   │   │   │   ├── _path.py
│   │   │   │   ├── _reqs.py
│   │   │   │   ├── _vendor/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── importlib_metadata/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _adapters.py
│   │   │   │   │   │   ├── _collections.py
│   │   │   │   │   │   ├── _compat.py
│   │   │   │   │   │   ├── _functools.py
│   │   │   │   │   │   ├── _itertools.py
│   │   │   │   │   │   ├── _meta.py
│   │   │   │   │   │   ├── _text.py
│   │   │   │   │   ├── importlib_resources/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _adapters.py
│   │   │   │   │   │   ├── _common.py
│   │   │   │   │   │   ├── _compat.py
│   │   │   │   │   │   ├── _itertools.py
│   │   │   │   │   │   ├── _legacy.py
│   │   │   │   │   │   ├── abc.py
│   │   │   │   │   │   ├── readers.py
│   │   │   │   │   │   ├── simple.py
│   │   │   │   │   ├── jaraco/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── context.py
│   │   │   │   │   │   ├── functools.py
│   │   │   │   │   │   ├── text/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── more_itertools/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── more.py
│   │   │   │   │   │   ├── recipes.py
│   │   │   │   │   ├── ordered_set.py
│   │   │   │   │   ├── packaging/
│   │   │   │   │   │   ├── __about__.py
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _manylinux.py
│   │   │   │   │   │   ├── _musllinux.py
│   │   │   │   │   │   ├── _structures.py
│   │   │   │   │   │   ├── markers.py
│   │   │   │   │   │   ├── requirements.py
│   │   │   │   │   │   ├── specifiers.py
│   │   │   │   │   │   ├── tags.py
│   │   │   │   │   │   ├── utils.py
│   │   │   │   │   │   ├── version.py
│   │   │   │   │   ├── pyparsing/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── actions.py
│   │   │   │   │   │   ├── common.py
│   │   │   │   │   │   ├── core.py
│   │   │   │   │   │   ├── diagram/
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── exceptions.py
│   │   │   │   │   │   ├── helpers.py
│   │   │   │   │   │   ├── results.py
│   │   │   │   │   │   ├── testing.py
│   │   │   │   │   │   ├── unicode.py
│   │   │   │   │   │   ├── util.py
│   │   │   │   │   ├── tomli/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _parser.py
│   │   │   │   │   │   ├── _re.py
│   │   │   │   │   │   ├── _types.py
│   │   │   │   │   ├── typing_extensions.py
│   │   │   │   │   ├── zipp.py
│   │   │   │   ├── archive_util.py
│   │   │   │   ├── build_meta.py
│   │   │   │   ├── cli-32.exe
│   │   │   │   ├── cli-64.exe
│   │   │   │   ├── cli-arm64.exe
│   │   │   │   ├── cli.exe
│   │   │   │   ├── command/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── alias.py
│   │   │   │   │   ├── bdist_egg.py
│   │   │   │   │   ├── bdist_rpm.py
│   │   │   │   │   ├── build.py
│   │   │   │   │   ├── build_clib.py
│   │   │   │   │   ├── build_ext.py
│   │   │   │   │   ├── build_py.py
│   │   │   │   │   ├── develop.py
│   │   │   │   │   ├── dist_info.py
│   │   │   │   │   ├── easy_install.py
│   │   │   │   │   ├── editable_wheel.py
│   │   │   │   │   ├── egg_info.py
│   │   │   │   │   ├── install.py
│   │   │   │   │   ├── install_egg_info.py
│   │   │   │   │   ├── install_lib.py
│   │   │   │   │   ├── install_scripts.py
│   │   │   │   │   ├── launcher manifest.xml
│   │   │   │   │   ├── py36compat.py
│   │   │   │   │   ├── register.py
│   │   │   │   │   ├── rotate.py
│   │   │   │   │   ├── saveopts.py
│   │   │   │   │   ├── sdist.py
│   │   │   │   │   ├── setopt.py
│   │   │   │   │   ├── test.py
│   │   │   │   │   ├── upload.py
│   │   │   │   │   ├── upload_docs.py
│   │   │   │   ├── config/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _apply_pyprojecttoml.py
│   │   │   │   │   ├── _validate_pyproject/
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── error_reporting.py
│   │   │   │   │   │   ├── extra_validations.py
│   │   │   │   │   │   ├── fastjsonschema_exceptions.py
│   │   │   │   │   │   ├── fastjsonschema_validations.py
│   │   │   │   │   │   ├── formats.py
│   │   │   │   │   ├── expand.py
│   │   │   │   │   ├── pyprojecttoml.py
│   │   │   │   │   ├── setupcfg.py
│   │   │   │   ├── dep_util.py
│   │   │   │   ├── depends.py
│   │   │   │   ├── discovery.py
│   │   │   │   ├── dist.py
│   │   │   │   ├── errors.py
│   │   │   │   ├── extension.py
│   │   │   │   ├── extern/
│   │   │   │   │   ├── __init__.py
│   │   │   │   ├── glob.py
│   │   │   │   ├── gui-32.exe
│   │   │   │   ├── gui-64.exe
│   │   │   │   ├── gui-arm64.exe
│   │   │   │   ├── gui.exe
│   │   │   │   ├── installer.py
│   │   │   │   ├── launch.py
│   │   │   │   ├── logging.py
│   │   │   │   ├── monkey.py
│   │   │   │   ├── msvc.py
│   │   │   │   ├── namespaces.py
│   │   │   │   ├── package_index.py
│   │   │   │   ├── py34compat.py
│   │   │   │   ├── sandbox.py
│   │   │   │   ├── script (dev).tmpl
│   │   │   │   ├── script.tmpl
│   │   │   │   ├── unicode_utils.py
│   │   │   │   ├── version.py
│   │   │   │   ├── wheel.py
│   │   │   │   ├── windows_support.py
│   │   │   ├── setuptools-65.5.0.dist-info/
│   │   │   │   ├── INSTALLER
│   │   │   │   ├── LICENSE
│   │   │   │   ├── METADATA
│   │   │   │   ├── RECORD
│   │   │   │   ├── REQUESTED
│   │   │   │   ├── WHEEL
│   │   │   │   ├── entry_points.txt
│   │   │   │   ├── top_level.txt
│   ├── Scripts/
│   │   ├── Activate.ps1
│   │   ├── activate
│   │   ├── activate.bat
│   │   ├── deactivate.bat
│   │   ├── pip.exe
│   │   ├── pip3.11.exe
│   │   ├── pip3.exe
│   │   ├── python.exe
│   │   ├── pythonw.exe
│   ├── lancar_ciborna.py/
│   │   ├── lancar_ciborna.py
│   ├── pyvenv.cfg
├── cosmos.py
├── cotacao_dol - Copia.xlsx
├── cotacao_dol.xlsx
├── dados_dolar.csv
├── data,abertura,maxima,minima,fechame.txt
├── gerar_readme.py
├── import MetaTrader5 as mt5.txt
├── iniciar_ciborna.bat
├── log_transcendental.csv
├── monitor_fluxo.py
├── monitor_fluxo_ia.py
├── montar_estrutura.py
├── mt5_stream.py
├── organiza_estrutura.py
├── requirements.txt
├── robo_ciborna.py
├── scripts/
│   ├── __init__.py
│   ├── estrategias.py
│   ├── fluxo_ordens.py
│   ├── rede_neural.py
├── scripts_ciborna/
│   ├── ciborna_launcher_readme.txt
│   ├── iniciar_ciborna.bat
│   ├── lancar_ciborna.py
├── stream_viagens.csv
├── ta_lib-0.6.4-cp311-cp311-win_amd64.whl
├── tests/
│   ├── run_all_tests.py
│   ├── simulador_execucao_estrategia.py
│   ├── simulador_previsao_vazia.py
│   ├── test_colunas_desalinhadas.py
│   ├── test_dataframe_erro_len.py
│   ├── test_dataframe_ok.py
│   ├── test_dataframe_vazio.py
│   ├── teste_grafico_plotly_fake.py
│   ├── verifica_dataframe_integridade.py
├── utils/
│   ├── __init__.py
│   ├── diagnostico_dataset.py
│   ├── log_neural.py
│   ├── manipulador_arquivos.py
│   ├── normalizador_dados.py
│   ├── tests/
│   │   ├── run_all_tests.py
│   │   ├── simulador_execucao_estrategia.py
│   │   ├── simulador_previsao_vazia.py
│   │   ├── test_colunas_desalinhadas.py
│   │   ├── test_dataframe_erro_len.py
│   │   ├── test_dataframe_ok.py
│   │   ├── test_validador_dataframe.py
│   │   ├── teste_grafico_plotly_fake.py
│   │   ├── verifica_dataframe_integridade.py
│   ├── validador_dados.py
│   ├── validador_tipos.py
├── utils_demo.py/
│   ├── utils_demo.py
├── vs_BuildTools.exe
```

## 🧠 Diagnóstico de Dados
- `resumo_estatistico(df)`
- `relatorio_nulos(df)`
- `verificar_constantes(df)`

---
**Ciborna** · Sistema supervisionado por astúcia, código e café ☕🛸