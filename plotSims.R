library(tidyverse)
library(ggpubr)
data0000 = read.table(file = "results0000.txt")
data0000$noloci <- as.factor(data0000$noloci)

p1=ggplot(data = data0000, aes(x=ID, y=theta_1A, color = noloci)) + geom_point() + geom_errorbar(data = data0000, width=0.4, mapping=aes(x=ID, ymax=theta_1A_UCI, ymin=theta_1A_LCI)) + geom_hline(aes(yintercept=0.001)) + scale_y_continuous("Posterior \u03b8 for species A", limits = c(0,0.005)) + labs(x = "Simulation Replicate") + theme(axis.text.x = element_blank())

p2=ggplot(data = data0000, aes(x=ID, y=theta_3C, color = noloci)) + geom_point() + geom_errorbar(data = data0000, width=0.4, mapping=aes(x=ID, ymax=theta_3C_UCI, ymin=theta_3C_LCI)) + geom_hline(aes(yintercept=0.001)) + scale_y_continuous("Posterior \u03b8 for species C", limits = c(0,0.005)) + labs(x = "Simulation Replicate") + theme(axis.text.x = element_blank())

p3=ggplot(data = data0000, aes(x=ID, y=theta_4R, color = noloci)) + geom_point() + geom_errorbar(data = data0000, width=0.4, mapping=aes(x=ID, ymax=theta_4R_UCI, ymin=theta_4R_LCI)) + geom_hline(aes(yintercept=0.001)) + scale_y_continuous("Posterior \u03b8 for species R", limits = c(0,0.005)) + labs(x = "Simulation Replicate") + theme(axis.text.x = element_blank())

p4=ggplot(data = data0000, aes(x=ID, y=theta_5S, color = noloci)) + geom_point() + geom_errorbar(data = data0000, width=0.4, mapping=aes(x=ID, ymax=theta_5S_UCI, ymin=theta_5S_LCI)) + geom_hline(aes(yintercept=0.001)) + scale_y_continuous("Posterior \u03b8 for species S", limits = c(0,0.005)) + labs(x = "Simulation Replicate") + theme(axis.text.x = element_blank())

p5=ggplot(data = data0000, aes(x=ID, y=theta_6H, color = noloci)) + geom_point() + geom_errorbar(data = data0000, width=0.4, mapping=aes(x=ID, ymax=theta_6H_UCI, ymin=theta_6H_LCI)) + geom_hline(aes(yintercept=0.001)) + scale_y_continuous("Posterior \u03b8 for species H", limits = c(0,0.005)) + labs(x = "Simulation Replicate") + theme(axis.text.x = element_blank())

p6=ggplot(data = data0000, aes(x=ID, y=phi_H, color = noloci)) + geom_point() + geom_errorbar(data = data0000, width=0.4, mapping=aes(x=ID, ymax=phi_H_UCI, ymin=phi_H_LCI)) + geom_hline(aes(yintercept=0.1))  + scale_y_continuous("Posterior of \u03d5", limits = c(0,0.5)) + labs(x = "Simulation Replicate") + theme(axis.text.x = element_blank())

p7=ggplot(data = data0000, aes(x=ID, y=tau_4R, color = noloci)) + geom_point() + geom_errorbar(data = data0000, width=0.4, mapping=aes(x=ID, ymax=tau_4R_UCI, ymin=tau_4R_LCI)) + geom_hline(aes(yintercept=0.03)) + scale_y_continuous("Posterior \u03c4 for species R", limits = c(0,0.05)) + labs(x = "Simulation Replicate") + theme(axis.text.x = element_blank())

p8=ggplot(data = data0000, aes(x=ID, y=tau_5S, color = noloci)) + geom_point() + geom_errorbar(data = data0000, width=0.4, mapping=aes(x=ID, ymax=tau_5S_UCI, ymin=tau_5S_LCI)) + geom_hline(aes(yintercept=0.02)) + scale_y_continuous("Posterior \u03c4 for species S", limits = c(0,0.05)) + labs(x = "Simulation Replicate") + theme(axis.text.x = element_blank())

p9=ggplot(data = data0000, aes(x=ID, y=tau_6H, color = noloci)) + geom_point() + geom_errorbar(data = data0000, width=0.4, mapping=aes(x=ID, ymax=tau_6H_UCI, ymin=tau_6H_LCI)) + geom_hline(aes(yintercept=0.01)) + scale_y_continuous("Posterior \u03c4 for species H", limits = c(0,0.05)) + labs(x = "Simulation Replicate") + theme(axis.text.x = element_blank())


cairo_pdf("test.pdf")
ggarrange(p1,p2,p3,p4,p5,p6,p7,p8,p9,ncol=3,nrow=3)
dev.off()


ggsave(filename="plot0000.pdf",device=cairo_pdf)
