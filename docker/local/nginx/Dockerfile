FROM nginx:1.21.3-alpine

# remove default default.conf and replace with one we create shortly
RUN rm /etc/nginx/conf.d/default.conf

COPY ./default.conf /etc/nginx/conf.d/defaut.conf