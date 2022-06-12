(function(){"use strict";var t={2683:function(t,e,n){n(6992),n(8674),n(9601),n(7727);var a=n(144),o=n(7166),r=n.n(o),s=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-app",[n("v-main",[n("router-view")],1)],1)},i=[],l={name:"App",created:function(){console.log(this.$route.path)}},c=l,u=n(1001),d=n(3453),p=n.n(d),h=n(7524),f=n(7877),v=(0,u.Z)(c,s,i,!1,null,null,null),m=v.exports;p()(v,{VApp:h.Z,VMain:f.Z});var b,g=n(9132);a.Z.use(g.Z);var _=null===(b=window.Telegram)||void 0===b?void 0:b.WebApp.themeParams,Z=new g.Z({theme:{dark:"dark"===_.colorScheme}}),y=n(8345),w=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"dashboard"},[n("Cards",{attrs:{cards:t.cards}}),n("Charts",{attrs:{charts:t.charts}})],1)},x=[],C=(n(1539),n(4747),n(3290),function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",[n("v-row",{attrs:{"no-gutters":""}},t._l(t.cards,(function(e){return n("v-col",{key:e.name},[n("v-card",{staticClass:"ma-4"},[n("v-card-title",{staticClass:"d-flex justify-space-between"},[n("div",[n("v-icon",{staticClass:"mr-2",attrs:{large:""}},[t._v(" "+t._s(e.icon)+" ")]),t._v(" "+t._s(e.value)+" ")],1),e.has_data_table?n("router-link",{attrs:{to:"/data-table/"+e.name}},[n("v-btn",{attrs:{icon:""}},[n("v-icon",[t._v("mdi-information")])],1)],1):t._e()],1),n("v-card-text",[t._v(" "+t._s(e.name)+" ")])],1)],1)})),1)],1)}),V=[],O={name:"Cards",props:["cards"]},$=O,T=n(680),k=n(3237),A=n(7118),D=n(2102),j=n(6428),E=n(2877),B=(0,u.Z)($,C,V,!1,null,"56d9592c",null),P=B.exports;p()(B,{VBtn:T.Z,VCard:k.Z,VCardText:A.ZB,VCardTitle:A.EB,VCol:D.Z,VIcon:j.Z,VRow:E.Z});var I=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",t._l(t.charts,(function(e){return n("v-row",{key:e.name},[n("v-col",[n("div",{staticClass:"pl-4 banner"},[t._v(t._s(e.name))]),n("apexchart",{attrs:{height:"300",type:e.type,series:e.series,options:e.options}})],1)],1)})),1)},S=[],M={props:["charts"]},W=M,F=(0,u.Z)(W,I,S,!1,null,null,null),R=F.exports;p()(F,{VCol:D.Z,VRow:E.Z});var q={name:"Dashboard",components:{Cards:P,Charts:R},data:function(){return{charts:[],auth:"",cards:[]}},methods:{fetchData:function(){var t=this;this.$http.get("/dashboard/").then((function(e){e.data.charts.forEach((function(t){var e={style:{colors:Array(t.options.xaxis.categories.length).fill("var(--tg-theme-hint-color)")}};t.options.xaxis.labels=e,t.options.yaxis={labels:e},t.options.colors=["var(--tg-theme-link-color)"]})),t.cards=e.data.cards,t.charts=e.data.charts}))}},created:function(){var t;this.auth=null===(t=window.Telegram)||void 0===t?void 0:t.WebApp.initData,this.fetchData()}},z=q,G=(0,u.Z)(z,w,x,!1,null,null,null),H=G.exports,J=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"data-table"},[n("v-app-bar",[n("v-btn",{attrs:{icon:"",to:"/"}},[n("v-icon",[t._v("mdi-arrow-left")])],1),n("v-toolbar-title",[t._v(t._s(t.$route.params.name))])],1),n("v-data-table",{staticClass:"elevation-1 ma-8",attrs:{headers:t.headers,items:t.items,options:t.options,"server-items-length":t.totalItems,loading:t.loading},on:{"update:options":function(e){t.options=e}}})],1)},K=[],L=(n(8309),{data:function(){return{totalItems:0,items:[],loading:!0,options:{},headers:[]}},watch:{options:{handler:function(){this.getDataFromApi()},deep:!0}},methods:{getDataFromApi:function(){var t=this;this.loading=!0,console.log(this.options);var e="/data-table/"+this.$route.params.name+"?per_page="+this.options.itemsPerPage+"&page="+this.options.page;this.options.sortBy[0]&&(e+="&sort_by="+this.options.sortBy[0]),this.options.sortDesc[0]&&(e+="&desc="+this.options.sortDesc[0]),this.$http.get(e).then((function(e){t.items=e.data.items,t.totalItems=e.data.totalItems,t.headers!==[]&&(t.headers=e.data.headers),t.loading=!1}))}}}),N=L,Q=n(3343),U=n(2543),X=n(7921),Y=(0,u.Z)(N,J,K,!1,null,null,null),tt=Y.exports;p()(Y,{VAppBar:Q.Z,VBtn:T.Z,VDataTable:U.Z,VIcon:j.Z,VToolbarTitle:X.qW}),a.Z.use(y.Z);var et,nt=[{path:"/",component:H},{path:"/data-table/:name",component:tt}],at=new y.Z({base:"/web",routes:nt,mode:"history"}),ot=n(9669),rt=n.n(ot);a.Z.prototype.$http=rt();var st=null===(et=window.Telegram)||void 0===et?void 0:et.WebApp.initData;a.Z.prototype.$http.defaults.headers.common.Authorization=st,a.Z.use(r()),a.Z.component("apexchart",r()),new a.Z({vuetify:Z,router:at,render:function(t){return t(m)}}).$mount("#app")}},e={};function n(a){var o=e[a];if(void 0!==o)return o.exports;var r=e[a]={exports:{}};return t[a].call(r.exports,r,r.exports,n),r.exports}n.m=t,function(){var t=[];n.O=function(e,a,o,r){if(!a){var s=1/0;for(u=0;u<t.length;u++){a=t[u][0],o=t[u][1],r=t[u][2];for(var i=!0,l=0;l<a.length;l++)(!1&r||s>=r)&&Object.keys(n.O).every((function(t){return n.O[t](a[l])}))?a.splice(l--,1):(i=!1,r<s&&(s=r));if(i){t.splice(u--,1);var c=o();void 0!==c&&(e=c)}}return e}r=r||0;for(var u=t.length;u>0&&t[u-1][2]>r;u--)t[u]=t[u-1];t[u]=[a,o,r]}}(),function(){n.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return n.d(e,{a:e}),e}}(),function(){n.d=function(t,e){for(var a in e)n.o(e,a)&&!n.o(t,a)&&Object.defineProperty(t,a,{enumerable:!0,get:e[a]})}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"===typeof window)return window}}()}(),function(){n.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)}}(),function(){n.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})}}(),function(){var t={143:0};n.O.j=function(e){return 0===t[e]};var e=function(e,a){var o,r,s=a[0],i=a[1],l=a[2],c=0;if(s.some((function(e){return 0!==t[e]}))){for(o in i)n.o(i,o)&&(n.m[o]=i[o]);if(l)var u=l(n)}for(e&&e(a);c<s.length;c++)r=s[c],n.o(t,r)&&t[r]&&t[r][0](),t[r]=0;return n.O(u)},a=self["webpackChunkbot_admin"]=self["webpackChunkbot_admin"]||[];a.forEach(e.bind(null,0)),a.push=e.bind(null,a.push.bind(a))}();var a=n.O(void 0,[998],(function(){return n(2683)}));a=n.O(a)})();
//# sourceMappingURL=app-legacy.6bfd4871.js.map