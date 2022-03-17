https://github.com/redisson/redisson/issues/11
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
in RedisClient.java
try {
        final ConnectionWatchdog watchdog = new ConnectionWatchdog(bootstrap, channels, timer);

        ChannelFuture connect = null;
        // TODO use better concurrent workaround
        synchronized (bootstrap) {
            connect = bootstrap.handler(new ChannelInitializer<Channel>() {
                @Override
                protected void initChannel(Channel ch) throws Exception {
                    ch.pipeline().addLast(watchdog, handler, connection);
                }
            }).connect();
        }
        connect.sync();

        watchdog.setReconnect(true);

        return connection;
    } catch (Throwable e) {
        throw new RedisException("Unable to connect", e);
    }

this "synchronized " protect what?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

