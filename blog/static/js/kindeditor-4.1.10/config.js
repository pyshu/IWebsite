KindEditor.ready(function(K) {
                K.create('textarea[name=content]',{
                    width:'100%',
                    height:'450px',
                    uploadJson: '/admin/upload/'
                });
        });